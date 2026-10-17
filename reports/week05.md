# 📅 Week X: [Topic Name]

## 🛠️ 1. What I Built
- **Summary**: This week's implementation was focused on reproducibility through retrieving (and downloading) and working on website info locally.
- **Key Tools Used**: Vs Code, Terminal etc.
- **Artifact Location**: - Github folder "data"
- Files named "fetch_data.py", "scrape_books.py", "clean_books.py" and "classify.py" under Github folder "src"
- **How to Run** (if applicable):
  - [V] Installation steps: Installing relevant python packages through following commands needed.
  - [V] Run command(s):
  pip install requests beautifulsoup4 pandas scikit-learn
  pip freeze > requirements.txt (This command is specifically for reproducibility purposes. Saves dependencies.)
  - [V] Expected output: Website info downloaded and saved locally in a .html file, and then we can store the scraped data in .csv files.

## 🔍 2. My Exploration
- **What I Investigated Further**:
  - I included additional genres, in other words, I downloaded additional .html files belonging to other genres. (The proof for this is rather from Week 6, because the relevant "data" folder had better stay on my local environment. Otherwise, I have to remove /data from .gitignore .)
  - I added CLI arguments with argparse and extended the download to other book genres/categories.
- **Link to Evidence** (optional): https://github.com/tcsai/portfolio-25-26-oskocak-cell/tree/main/StreamLit%20Photos#:~:text=StreamLit,-Photos 
https://github.com/tcsai/portfolio-25-26-oskocak-cell/blob/main/src/fetch_data.py 

## 🤖 3. Use of GenAI (if applicable)
- **What I Asked It To Do**:
  - 2025-09-25: Used ChatGPT to receive brief explanations about some python modules and packages such as argparse.
  - 2025-09-25: Used ChatGPT to understand whether a problem occured under "PROBLEMS" tab on Vs Code was critical or not.
- **What I Got and Did With It**:
  - I compared ChatGPT's explanations about python modules/packages with other relevant info online.
  - I made sure via ChatGPT that the problem occured under "PROBLEMS" tab on Vs Code wouldn't effect my code and/or push to Github.
- **Risks or Misuses You Noticed**:
  - Info-wise, ChatGPT is very knowledable. But when asked about long lines of code within a project, AI tends to produce fast results and I realised that the codes might be problematic, especially when used as part of a whole even if you provide the AI with all components of your code and/or project. So that's another good example showing the importance of developping reproducible "habits".  Because ChatGPT usually tends to generate or suggest possible solutions, nevertheless the specificities of the project is much more related to the project owner's vision.

## 💬 4. Reflection
- **How did this week’s work support reproducibility or deployment?**
To me, this week's work was crucial on several points:
1. We started by creating and activating our virtual environment. This felt like wearing the belt before starting to drive.
2. We stored the data locally. So we took our measures against possible future incertainties and in a way delimited and delineated our work area with sufficiently definable criteria. Ex: The data was retrieved from a certain place at a certain day and time. Easy to reference.
3. Beyon these, we worked step by step keeping our main work are scaffold proper and clean. Thus, certain files were stored under certain folders and/or categories, and we made changes step by step to our relevant files when necessary. We updated our Makefile, for instance.
4. If we hadn't been that much organized, we could have failed to create a pipeline and automate our previous work.
- **What was most confusing or interesting?**
- It was interesting for me that website data was that much easily accessible. When used properly and responsibly from a reproducibility perspective, this could lead to many more explorations.
