# Healthcare Disparities Analysis - Data Cleaning & Preparation
# Purpose: Load, clean, and integrate multiple healthcare datasets

library(tidyverse)
library(tidyr)
library(dplyr)

# ============================================================================
# 1. DATA IMPORT
# ============================================================================

# Load patient demographics
patient_demographics <- read_csv("data/patient_demographics.csv") %>%
  rename_all(tolower)

# Load diagnoses data
diagnoses <- read_csv("data/diagnoses.csv") %>%
  rename_all(tolower)

# Load healthcare barriers (transportation, language, insurance)
barriers <- read_csv("data/barriers.csv") %>%
  rename_all(tolower)

# Load social determinants of health
sdoh <- read_csv("data/social_determinants.csv") %>%
  rename_all(tolower)

cat("Data imported successfully\n")
cat(sprintf("Patients: %d | Diagnoses: %d | Barriers: %d | SDOH: %d\n",
            nrow(patient_demographics), nrow(diagnoses),
            nrow(barriers), nrow(sdoh)))

# ============================================================================
# 2. EXPLORATORY CHECKS
# ============================================================================

# Check for missing values
missing_summary <- function(df, name) {
  missing_pct <- colSums(is.na(df)) / nrow(df) * 100
  cat("\n", name, " - Missing Values:\n")
  print(missing_pct[missing_pct > 0])
}

missing_summary(patient_demographics, "Demographics")
missing_summary(diagnoses, "Diagnoses")
missing_summary(barriers, "Barriers")
missing_summary(sdoh, "SDOH")

# ============================================================================
# 3. DATA CLEANING
# ============================================================================

# Clean demographics
demographics_clean <- patient_demographics %>%
  # Remove rows with missing patient ID
  filter(!is.na(patient_id)) %>%
  # Standardize race/ethnicity categories
  mutate(
    race_ethnicity = case_when(
      race_ethnicity == "W" ~ "White",
      race_ethnicity == "B" ~ "Black",
      race_ethnicity == "H" ~ "Hispanic",
      race_ethnicity == "A" ~ "Asian",
      race_ethnicity == "M" ~ "Multiracial",
      TRUE ~ "Other"
    ),
    # Convert age to numeric
    age = as.numeric(age),
    # Create age groups
    age_group = cut(age,
                    breaks = c(0, 18, 35, 50, 65, 100),
                    labels = c("0-18", "19-35", "36-50", "51-65", "65+"),
                    include.lowest = TRUE)
  ) %>%
  # Filter valid age range
  filter(age >= 0 & age <= 120)

# Clean diagnoses
diagnoses_clean <- diagnoses %>%
  filter(!is.na(patient_id)) %>%
  # Standardize diagnosis codes
  mutate(icd_code = str_trim(icd_code)) %>%
  # Create diagnosis categories
  mutate(
    diagnosis_category = case_when(
      str_starts(icd_code, "I") ~ "Circulatory",
      str_starts(icd_code, "J") ~ "Respiratory",
      str_starts(icd_code, "E") ~ "Endocrine",
      str_starts(icd_code, "K") ~ "Digestive",
      str_starts(icd_code, "M") ~ "Musculoskeletal",
      TRUE ~ "Other"
    )
  )

# Clean barriers data
barriers_clean <- barriers %>%
  filter(!is.na(patient_id)) %>%
  mutate(
    # Binary indicators for barriers
    has_transportation_barrier = as.numeric(transportation_barrier == "Yes"),
    has_language_barrier = as.numeric(language_barrier == "Yes"),
    insurance_type = case_when(
      insurance_type == "PV" ~ "Private",
      insurance_type == "MG" ~ "Medicaid",
      insurance_type == "CR" ~ "Medicare",
      insurance_type == "UN" ~ "Uninsured",
      TRUE ~ "Other"
    ),
    total_barriers = has_transportation_barrier +
                     has_language_barrier +
                     as.numeric(!is.na(insurance_type))
  )

# Clean SDOH data
sdoh_clean <- sdoh %>%
  filter(!is.na(patient_id)) %>%
  mutate(
    # Numeric indicators
    poverty = as.numeric(below_poverty_line == "Yes"),
    food_insecurity = as.numeric(food_insecurity == "Yes"),
    housing_instability = as.numeric(housing_instability == "Yes"),
    sdoh_score = poverty + food_insecurity + housing_instability
  )

cat("\nData cleaning completed\n")

# ============================================================================
# 4. DATA INTEGRATION
# ============================================================================

# Merge all datasets
healthcare_data <- patient_demographics %>%
  left_join(demographics_clean, by = "patient_id") %>%
  left_join(diagnoses_clean, by = "patient_id") %>%
  left_join(barriers_clean, by = "patient_id") %>%
  left_join(sdoh_clean, by = "patient_id") %>%
  # Remove duplicate columns
  select(-contains(".y")) %>%
  rename_all(~str_remove(., "\\.x$"))

# ============================================================================
# 5. CREATE OUTCOME VARIABLE
# ============================================================================

# Define healthcare access score (lower = more disparities)
healthcare_access <- healthcare_data %>%
  group_by(patient_id) %>%
  summarise(
    num_visits = n_distinct(visit_id),
    has_chronic_diagnosis = as.numeric(any(diagnosis_category %in% c("Circulatory", "Endocrine"))),
    preventive_care_visits = sum(visit_type == "Preventive", na.rm = TRUE),
    .groups = "drop"
  ) %>%
  mutate(
    access_score = (num_visits * 0.4 + preventive_care_visits * 0.6)
  )

# Merge back
final_data <- healthcare_data %>%
  left_join(healthcare_access, by = "patient_id") %>%
  # Create disparity indicator (low access = disparity)
  mutate(
    low_access = as.numeric(access_score < median(access_score, na.rm = TRUE))
  )

# ============================================================================
# 6. QUALITY ASSURANCE
# ============================================================================

cat("\n=== FINAL DATASET SUMMARY ===\n")
cat(sprintf("Total patients: %d\n", n_distinct(final_data$patient_id)))
cat(sprintf("Total records: %d\n", nrow(final_data)))
cat(sprintf("Missing values: %d%%\n", round(sum(is.na(final_data)) / (nrow(final_data) * ncol(final_data)) * 100, 2)))

# Check for duplicates
duplicates <- final_data %>%
  group_by(patient_id) %>%
  filter(n() > 1) %>%
  nrow()
cat(sprintf("Duplicate records: %d\n", duplicates))

# ============================================================================
# 7. SAVE PROCESSED DATA
# ============================================================================

write_csv(final_data, "data/healthcare_disparities_processed.csv")
cat("\n✓ Processed data saved to data/healthcare_disparities_processed.csv\n")

# Save summary statistics
summary_stats <- final_data %>%
  summarise(
    n_patients = n_distinct(patient_id),
    avg_age = mean(age, na.rm = TRUE),
    pct_low_access = mean(low_access, na.rm = TRUE) * 100,
    pct_transportation_barrier = mean(has_transportation_barrier, na.rm = TRUE) * 100,
    pct_poverty = mean(poverty, na.rm = TRUE) * 100
  )

write_csv(summary_stats, "results/summary_statistics.csv")
cat("✓ Summary statistics saved\n")

cat("\n=== DATA CLEANING COMPLETE ===\n")
cat("Next step: Run 02_exploratory_analysis.R\n")
