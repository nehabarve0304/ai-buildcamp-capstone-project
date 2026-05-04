# AI Resume Matcher & Job Fit Analyzer

## The Problem

Job seekers often struggle not only to find relevant job opportunities but also to understand how well their profile matches those roles and what they need to improve. Existing platforms like LinkedIn and Indeed help users discover jobs, but they do not provide personalised, actionable insights on skill gaps, profile alignment, or how to improve chances of getting shortlisted. This problem affects students, early-career professionals, and experienced candidates who apply to multiple roles without clear feedback on why they are not a good fit.

## What It Does

The system takes a user's CV (resume text or PDF) and optional preferences (target role, job title, location, seniority level). It then:
- Retrieves a list of relevant job postings based on the user’s profile and preferences.
- Extracts and structures key skills and experience from the CV.
- Analyses requirements from selected job descriptions.
- Compares the user’s profile with job requirements to generate a match score for each job, a clear gap analysis (missing or weak skills), actionable suggestions to improve the CV/profile, and optional interview preparation questions tailored to the role.

The output is a structured report that helps the user both discover suitable jobs and understand how to improve their chances of success for each role.

## Setup

1. Install uv if you don't have it yet: https://docs.astral.sh/uv/getting-started/installation/

2. Clone this repository (or download the zip and extract it).

3. Create a `.env` file from the template and add your API key:

       cp .env.example .env

4. Install dependencies:

       uv sync

5. Start Jupyter:

       uv run jupyter notebook

## Notebooks

- `notebooks/01-setup.ipynb` - smoke test that confirms your environment works
- `notebooks/02-rag.ipynb` - a minimal RAG baseline you can adapt to your own data

## Data

Put your project data in the `data/` folder. See `notebooks/02-rag.ipynb` for how to load it.
