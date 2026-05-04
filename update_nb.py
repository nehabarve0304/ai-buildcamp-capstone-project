import json

with open('notebooks/02-rag.ipynb', 'r') as f:
    nb = json.load(f)

nb['cells'][3]['source'] = [
    "import json\n",
    "\n",
    "with open('../data/jobs.json', 'r') as f:\n",
    "    documents = json.load(f)\n"
]

nb['cells'][5]['source'] = [
    "index = Index(\n",
    "    text_fields=[\"job_title\", \"company\", \"description\", \"requirements\"],\n",
    "    keyword_fields=[\"location\", \"seniority_level\"],\n",
    ")\n",
    "\n",
    "index.fit(documents)"
]

nb['cells'][8]['source'] = [
    "instructions = \"\"\"\n",
    "You are an expert career advisor and job matching assistant.\n",
    "The user will provide their CV or profile, and possibly some preferences.\n",
    "Your task is to review the provided job postings in the CONTEXT,\n",
    "and perform a personalized gap analysis.\n",
    "For each relevant job:\n",
    "1. Provide a Match Score (e.g., 80%).\n",
    "2. Explain why they are a good fit.\n",
    "3. Identify clear skill gaps (missing or weak skills based on the job requirements).\n",
    "4. Give actionable suggestions to improve their chances.\n",
    "5. Provide 2-3 interview preparation questions tailored to the role.\n",
    "\"\"\".strip()\n",
    "\n",
    "\n",
    "def build_prompt(query, search_results):\n",
    "    clean_results = []\n",
    "    for doc in search_results:\n",
    "        clean_results.append({\n",
    "            \"job_title\": doc.get(\"job_title\"),\n",
    "            \"company\": doc.get(\"company\"),\n",
    "            \"requirements\": doc.get(\"requirements\"),\n",
    "            \"description\": doc.get(\"description\"),\n",
    "        })\n",
    "    search_result_json = json.dumps(clean_results, indent=2)\n",
    "\n",
    "    user_prompt = f\"\"\"\n",
    "<USER_PROFILE>\n",
    "{query}\n",
    "</USER_PROFILE>\n",
    "\n",
    "<AVAILABLE_JOBS>\n",
    "{search_result_json}\n",
    "</AVAILABLE_JOBS>\n",
    "\"\"\".strip()\n",
    "\n",
    "    return user_prompt"
]

nb['cells'][12]['source'] = [
    "user_cv = \"\"\"\n",
    "I am a Python developer with 3 years of experience. \n",
    "I have worked extensively with Django, Flask, and PostgreSQL. \n",
    "I also have some frontend experience with basic HTML/CSS and vanilla JavaScript. \n",
    "I'm looking for a Mid-Level Backend or Fullstack Engineer role in London or Remote.\n",
    "\"\"\"\n",
    "print(rag(user_cv))"
]

with open('notebooks/02-rag.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)
