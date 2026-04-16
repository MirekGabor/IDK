# Setting Up Your GitHub Repositories - Complete Guide

This guide walks you through creating and pushing your three professional portfolio projects to GitHub.

## 📋 Overview

You'll be creating **3 professional GitHub repositories**:

1. **healthcare-disparities-analysis** - Machine learning + data science
2. **cognitive-pupil-research** - Research methodology + statistics
3. **dojo-explore** - Leadership + program management

Each repository is organized in the `IDK` folder locally and ready to push to GitHub.

---

## 🚀 Prerequisites

Make sure you have:
- ✅ GitHub account (create at github.com if needed)
- ✅ Git installed (`git --version` to check)
- ✅ Git configured with your name/email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 📝 Step 1: Prepare Your Repositories Locally

Each project folder is already structured. Let's initialize them as git repositories:

### For healthcare-disparities-analysis

```bash
cd /Users/miroslavgabor/Documents/GitHub/IDK/healthcare-disparities-analysis

# Initialize git repo
git init

# Copy the .gitignore
cp ../.github-template-gitignore .gitignore

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Healthcare disparities analysis project

- R scripts for data cleaning, analysis, and visualization
- Decision tree ML models for healthcare access prediction
- R/Shiny interactive dashboard
- APA-style documentation"
```

### For cognitive-pupil-research

```bash
cd /Users/miroslavgabor/Documents/GitHub/IDK/cognitive-pupil-research

git init
cp ../.github-template-gitignore .gitignore
git add .
git commit -m "Initial commit: Cognitive effort and pupil dilation research

- Complete APA-style research study
- Statistical analysis (repeated measures ANOVA)
- Eye-tracking data processing
- Publication-quality visualizations with ggplot2"
```

### For dojo-explore

```bash
cd /Users/miroslavgabor/Documents/GitHub/IDK/dojo-explore

git init
cp ../.github-template-gitignore .gitignore
git add .
git commit -m "Initial commit: DojoExplore biotechnology workshop program

- Python-based program analytics
- Attendance and feedback tracking
- Budget management templates
- Program guide for reproducibility"
```

---

## 🔑 Step 2: Create Remote Repositories on GitHub

### Option A: Using Web Browser (Easiest for Beginners)

1. Go to **github.com** and log in
2. Click **"+" → "New repository"** (top right)
3. Create first repository: `healthcare-disparities-analysis`
   - **Repository name:** healthcare-disparities-analysis
   - **Description:** Machine learning analysis of healthcare disparities using EHR data
   - **Public** ✓ (makes it visible to employers)
   - **Add README.md** ✗ (you already have one)
   - **Add .gitignore** ✗ (you already have one)
   - **Choose license:** MIT
   - Click **"Create repository"**

4. Repeat for `cognitive-pupil-research`
   - **Description:** APA-style research study on cognitive load and pupil dilation using eye-tracking

5. Repeat for `dojo-explore`
   - **Description:** Leadership project coordinating 6-week biotechnology workshop program

### Option B: Using GitHub CLI (Faster)

If you have GitHub CLI installed:

```bash
# Install GitHub CLI (if needed)
# macOS: brew install gh
# Or from https://cli.github.com

# Authenticate
gh auth login

# Create repositories
gh repo create healthcare-disparities-analysis --public --description "Machine learning analysis of healthcare disparities" --source=. --remote=origin --push

gh repo create cognitive-pupil-research --public --description "APA-style research on cognitive load and pupil dilation" --source=. --remote=origin --push

gh repo create dojo-explore --public --description "Leadership project: 6-week biotech workshop program" --source=. --remote=origin --push
```

---

## 🔗 Step 3: Connect Local Repos to GitHub

After creating the remote repositories, connect your local folders:

### For healthcare-disparities-analysis

```bash
cd /Users/miroslavgabor/Documents/GitHub/IDK/healthcare-disparities-analysis

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/healthcare-disparities-analysis.git

# Verify
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

### For cognitive-pupil-research

```bash
cd /Users/miroslavgabor/Documents/GitHub/IDK/cognitive-pupil-research

git remote add origin https://github.com/YOUR_USERNAME/cognitive-pupil-research.git
git branch -M main
git push -u origin main
```

### For dojo-explore

```bash
cd /Users/miroslavgabor/Documents/GitHub/IDK/dojo-explore

git remote add origin https://github.com/YOUR_USERNAME/dojo-explore.git
git branch -M main
git push -u origin main
```

---

## ✅ Step 4: Verify Your Repositories

Visit GitHub and check:
- [ ] **healthcare-disparities-analysis** shows up on your profile
- [ ] **cognitive-pupil-research** shows up on your profile
- [ ] **dojo-explore** shows up on your profile
- [ ] Each has a good README visible
- [ ] Code files are visible in the repository

Visit URLs like:
```
https://github.com/YOUR_USERNAME/healthcare-disparities-analysis
https://github.com/YOUR_USERNAME/cognitive-pupil-research
https://github.com/YOUR_USERNAME/dojo-explore
```

---

## 📊 Step 5: Add These to Your Portfolio

Update your portfolio website to link to GitHub repos:

```html
<a href="https://github.com/YOUR_USERNAME/healthcare-disparities-analysis">
  View on GitHub →
</a>
```

Update your LinkedIn with repo links in each project description.

---

## 🎯 Step 6: Optimize Your GitHub Profile

Your GitHub profile is now your portfolio. Optimize it:

### 1. Profile Picture
- Upload a professional headshot
- Settings → Profile picture

### 2. Bio
Set your bio to something like:
```
CS Major | Math Minor | Macalester College
AI & Data Science Enthusiast | Building intelligent solutions with data
```

### 3. Pin Your Best Repositories
- Go to your GitHub profile
- Click "Customize your pins"
- Pin your 3 project repositories (they'll show on your profile)

### 4. Add Profile README (Optional but Impressive)
Create a file called `README.md` in a special repo:

```bash
# Create repo (if it doesn't exist)
gh repo create miroslavgabor --public

# Add content
cat > README.md << 'EOF'
# 👋 Miroslav Gabor

I'm a Computer Science major at Macalester College passionate about **AI & Data Science**.

## 📊 Featured Projects

- **[Healthcare Disparities Analysis](https://github.com/miroslavgabor/healthcare-disparities-analysis)** - ML analysis of healthcare equity using EHR data
- **[Cognitive Pupil Research](https://github.com/miroslavgabor/cognitive-pupil-research)** - APA-style research on cognitive load using eye-tracking
- **[DojoExplore](https://github.com/miroslavgabor/dojo-explore)** - Leadership project: 6-week biotech workshop program

## 🛠️ Tech Stack
- **Languages:** Python, R, SQL
- **Data Science:** Machine Learning, Statistical Analysis, Data Visualization
- **Tools:** R/Shiny, Pandas, Scikit-learn, ggplot2

## 🎓 About Me
- 📚 Freshman at Macalester College (CS Major, Math Minor)
- 🏆 Perfect 4.0 GPA | Bonner & Davis Scholar
- 🌍 Multilingual (English, Spanish, Czech)
- 💼 Currently: Teaching Assistant at Groveland Elementary School

## 📈 Let's Connect
- 📧 [Email](mailto:mgabor@macalester.edu)
- 💼 [LinkedIn](https://linkedin.com/in/your-username)
- 🔗 [Portfolio](https://your-portfolio.com)
EOF

git add README.md
git commit -m "Add profile README"
git push origin main
```

---

## 🔄 Step 7: Keep Repositories Updated

As you improve projects, push updates:

```bash
cd /path/to/project

# Make changes, then:
git add .
git commit -m "Description of changes"
git push origin main

# For example:
git commit -m "Improve model accuracy with hyperparameter tuning"
git push origin main
```

---

## 📚 Best Practices for GitHub

### 1. Write Meaningful Commit Messages
✅ Good:
```
Fix: Improve decision tree accuracy from 82% to 87%
Add: Interactive visualizations for healthcare barriers
```

❌ Bad:
```
fixed stuff
update
```

### 2. Update READMEs Regularly
- Keep them current with project status
- Add new findings/results as you progress
- Include usage instructions

### 3. Use Issues for Development
- Create "Issues" for problems/features
- Close them with commits: `git commit -m "Fixes #5"`

### 4. Create Branches for Experiments
```bash
git checkout -b feature/new-ml-model
# Make changes
git add .
git commit -m "Add random forest model"
git push origin feature/new-ml-model
# Create Pull Request on GitHub
```

---

## 💡 What Makes GitHub Profiles Stand Out to Employers

✅ **Employers Look For:**
- Clean, well-documented code
- Comprehensive READMEs
- Multiple projects showing depth
- Regular commits (shows active development)
- Professional commit messages
- Working projects with examples

❌ **Employers Avoid:**
- Repos with no README
- Poorly organized code
- One-off projects
- Vague commit messages
- Inactive repos

---

## 🎬 Quick Checklist

Complete this to be GitHub-ready:

- [ ] All 3 repos created locally and initialized with git
- [ ] All 3 repos pushed to GitHub
- [ ] Each repo has a comprehensive README.md
- [ ] Each repo has a .gitignore
- [ ] GitHub profile has a photo
- [ ] GitHub profile has a bio mentioning AI/Data Science
- [ ] 3 repos pinned on your profile
- [ ] Links to all repos in your portfolio website
- [ ] Links to GitHub in your LinkedIn profile

---

## 🆘 Troubleshooting

### "remote already exists"
```bash
git remote remove origin
git remote add origin https://...
```

### "authentication failed"
Generate a personal access token:
1. GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (repo access)
3. Use token as password when prompted

### "fatal: not a git repository"
Make sure you're in the right directory:
```bash
pwd  # Check current location
git status  # Should work if it's a git repo
```

---

## 🎉 You're Done!

Your GitHub is now your professional portfolio. Next steps:

1. **Share your GitHub** with internship recruiters
2. **Keep building projects** (add more ML/AI projects)
3. **Participate in Kaggle** competitions
4. **Contribute to open source** (nice to have)

---

## 📞 Need Help?

- **GitHub Docs:** https://docs.github.com
- **Git Cheat Sheet:** https://git-scm.com/book
- **My Portfolio:** Link when ready

---

**Status:** Ready to become highly visible to employers! 🚀
