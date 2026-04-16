"""
DojoExplore - Attendance Analysis Script

This script analyzes attendance patterns across all DojoExplore sessions,
generating summary statistics and visualizations.

Author: Miroslav Gabor
Date: 2024
"""

import pandas as pd
import numpy as np
from datetime import datetime

# ============================================================================
# 1. LOAD DATA
# ============================================================================

print("=" * 70)
print("DojoExplore - Attendance Analysis")
print("=" * 70)

# Load attendance data
attendance_df = pd.read_csv('../data/attendance.csv')

# Display basic info
print(f"\nDataset loaded: {len(attendance_df)} records")
print(f"Columns: {list(attendance_df.columns)}")

# ============================================================================
# 2. DATA CLEANING
# ============================================================================

# Standardize column names
attendance_df.columns = attendance_df.columns.str.lower().str.strip()

# Ensure session_date is datetime
attendance_df['session_date'] = pd.to_datetime(attendance_df['session_date'])

# Remove any null values
attendance_df = attendance_df.dropna(subset=['session_name', 'participant_id'])

print(f"Records after cleaning: {len(attendance_df)}")

# ============================================================================
# 3. ATTENDANCE SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("ATTENDANCE SUMMARY")
print("=" * 70)

# Overall statistics
total_sessions = attendance_df['session_name'].nunique()
unique_participants = attendance_df['participant_id'].nunique()
total_attendance = len(attendance_df)
avg_attendance = total_attendance / total_sessions

print(f"\nOverall Statistics:")
print(f"  Total Sessions: {total_sessions}")
print(f"  Unique Participants: {unique_participants}")
print(f"  Total Attendance: {total_attendance}")
print(f"  Average Attendance per Session: {avg_attendance:.1f}")

# ============================================================================
# 4. ATTENDANCE BY SESSION
# ============================================================================

print(f"\n{'Session':<30} {'Attendance':<12} {'% of Total':<12}")
print("-" * 60)

attendance_by_session = attendance_df.groupby('session_name').size().sort_values(ascending=False)

for session, count in attendance_by_session.items():
    pct = (count / total_attendance) * 100
    print(f"{session:<30} {count:<12} {pct:>10.1f}%")

# ============================================================================
# 5. PARTICIPANT ENGAGEMENT
# ============================================================================

print(f"\n" + "=" * 70)
print("PARTICIPANT ENGAGEMENT")
print("=" * 70)

# Sessions attended per participant
sessions_per_participant = attendance_df.groupby('participant_id').size()

print(f"\nEngagement Distribution:")
print(f"  Attended 1 session: {(sessions_per_participant == 1).sum()} participants")
print(f"  Attended 2-3 sessions: {((sessions_per_participant >= 2) & (sessions_per_participant <= 3)).sum()} participants")
print(f"  Attended 4+ sessions: {(sessions_per_participant >= 4).sum()} participants")
print(f"  Attended all sessions: {(sessions_per_participant == total_sessions).sum()} participants")

avg_sessions_attended = sessions_per_participant.mean()
print(f"\nAverage sessions per participant: {avg_sessions_attended:.2f}")

# ============================================================================
# 6. ATTENDANCE TRENDS
# ============================================================================

print(f"\n" + "=" * 70)
print("ATTENDANCE TREND")
print("=" * 70)

# Sort by date
attendance_by_date = attendance_df.sort_values('session_date').groupby('session_date').size()

print(f"\nAttendance by Week:")
for date, count in attendance_by_date.items():
    week_num = (date - attendance_by_date.index[0]).days // 7 + 1
    pct_change = ""
    if len(attendance_by_date) > 1:
        prev_idx = list(attendance_by_date.index).index(date) - 1
        if prev_idx >= 0:
            prev_count = attendance_by_date.iloc[prev_idx]
            change = count - prev_count
            pct_change = f" ({change:+.0f})"
    print(f"  Week {week_num} ({date.strftime('%m/%d')}): {count} participants{pct_change}")

# ============================================================================
# 7. SESSION QUALITY (Using Feedback Data if Available)
# ============================================================================

try:
    feedback_df = pd.read_csv('../data/participant_feedback.csv')
    feedback_df.columns = feedback_df.columns.str.lower().str.strip()

    print(f"\n" + "=" * 70)
    print("PARTICIPANT FEEDBACK SUMMARY")
    print("=" * 70)

    if 'overall_rating' in feedback_df.columns:
        avg_rating = feedback_df['overall_rating'].mean()
        print(f"\nAverage Overall Rating: {avg_rating:.2f}/5.0")

        rating_dist = feedback_df['overall_rating'].value_counts().sort_index(ascending=False)
        print(f"\nRating Distribution:")
        for rating, count in rating_dist.items():
            pct = (count / len(feedback_df)) * 100
            print(f"  {rating:.0f} stars: {count} ({pct:.0f}%)")

    if 'recommendation' in feedback_df.columns:
        recommend_pct = (feedback_df['recommendation'].str.lower() == 'yes').sum() / len(feedback_df) * 100
        print(f"\nWould Recommend Program: {recommend_pct:.0f}%")

except FileNotFoundError:
    print("\nNote: Feedback data not found. Skipping feedback analysis.")

# ============================================================================
# 8. RETENTION RATE
# ============================================================================

print(f"\n" + "=" * 70)
print("RETENTION ANALYSIS")
print("=" * 70)

# Compare attendance in first vs. last session
first_session_date = attendance_df['session_date'].min()
last_session_date = attendance_df['session_date'].max()

first_session_ids = set(attendance_df[attendance_df['session_date'] == first_session_date]['participant_id'])
last_session_ids = set(attendance_df[attendance_df['session_date'] == last_session_date]['participant_id'])

retained = len(first_session_ids & last_session_ids)
retention_rate = (retained / len(first_session_ids)) * 100 if len(first_session_ids) > 0 else 0

print(f"\nFirst Session Attendance: {len(first_session_ids)}")
print(f"Last Session Attendance: {len(last_session_ids)}")
print(f"Participants in Both: {retained}")
print(f"Retention Rate: {retention_rate:.1f}%")

# ============================================================================
# 9. KEY METRICS SUMMARY
# ============================================================================

print(f"\n" + "=" * 70)
print("KEY METRICS SUMMARY")
print("=" * 70)

summary_metrics = {
    'Total Participants': unique_participants,
    'Total Sessions': total_sessions,
    'Average Attendance': round(avg_attendance, 1),
    'Total Attendance': total_attendance,
    'Avg Sessions/Participant': round(avg_sessions_attended, 2),
    'Retention Rate': f"{retention_rate:.1f}%",
}

for metric, value in summary_metrics.items():
    print(f"  {metric:<25} {value}")

# ============================================================================
# 10. SAVE REPORT
# ============================================================================

# Generate text report
report = []
report.append("=" * 70)
report.append("DojoExplore - Attendance Analysis Report")
report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
report.append("=" * 70)
report.append("")

report.append("OVERALL STATISTICS")
report.append("-" * 70)
for metric, value in summary_metrics.items():
    report.append(f"{metric:<25} {value}")

report.append("")
report.append("ATTENDANCE BY SESSION")
report.append("-" * 70)
for session, count in attendance_by_session.items():
    pct = (count / total_attendance) * 100
    report.append(f"{session:<30} {count:<12} {pct:>10.1f}%")

# Write report to file
report_text = "\n".join(report)
with open('../results/attendance_report.txt', 'w') as f:
    f.write(report_text)

print(f"\n✓ Report saved to ../results/attendance_report.txt")

print("\n" + "=" * 70)
print("ANALYSIS COMPLETE")
print("=" * 70)
