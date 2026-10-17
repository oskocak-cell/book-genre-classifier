# Reproducibility & Model Deployment — Master's Course Portfolio

**Ozan Safak Kocak · MSc Data Science and Society · Tilburg University · 2025**

This portfolio documents six weeks of work for the Research Seminar in Reproducibility & Model Deployment. It combines course exercises, weekly reflections, and a small book genre classification pipeline using TF-IDF and logistic regression, served through FastAPI and a Streamlit interface. It is an educational prototype, with the original learning narrative retained below.

## Run the final project

Use Python 3.11–3.13. Run all commands from the repository root. The saved model was created with scikit-learn 1.6.1, which is pinned in `requirements.txt`.

```sh
git clone https://github.com/oskocak-cell/book-genre-classifier.git
cd book-genre-classifier
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn src.api:app --reload --port 8000
```

On Windows, activate the environment with `.venv\Scripts\activate` instead. Leave the API running and open a second terminal in the same folder, activate the environment there, then run:

```sh
python -m streamlit run src/app.py
```

Open the address printed by Streamlit (normally http://localhost:8501). The API documentation is at http://localhost:8000/docs, with a health check at http://localhost:8000/health. The interface requires the API to be running.

### Rebuild the dataset and model

The saved models are included, so collecting data is optional for trying the interface. To reproduce training, run these commands in order; downloading requires internet access:

```sh
python src/fetch_data.py
python src/scrape_books.py
python src/clean_books.py
python src/classify.py
```

Training prints evaluation results and writes `logs/metrics.csv` and the saved models. Downloaded and processed data and logs are excluded from Git. Start with an empty `data/raw/` directory for a fresh collection: the downloader uses timestamped filenames and the parser reads all matching HTML files, so repeated downloads can duplicate titles. Only the first page of each configured category is collected.

### Docker

```sh
docker build -t book-genre-classifier .
docker run --rm -p 8000:8000 book-genre-classifier
```

This starts the API with the included model. Run the Streamlit interface separately as above.

## Portfolio guide and limitations

- [`src/`](src/): the final data pipeline, API, interface, and statistics exercise.
- [`tests/`](tests/): the original statistics and smoke tests; these do not validate the complete application.
- [`reports/`](reports/): weekly course reflections. The peer feedback report about another student is omitted from this personal copy.
- [`my_project_week2/`](my_project_week2/): an earlier command-line exercise.
- [`deployment/app.py`](deployment/app.py): an early stub, not the final interface; use `src/app.py`.
- `environment.yml`, the Poetry lockfile, and the training Docker example are historical course artifacts. Use the requirements-based setup above for the final application.

This is a small classroom demonstration, not a production service. Genre predictions can be inaccurate, and the screenshots record examples from the course rather than guaranteed predictions. `/metrics` reports the current training metrics when available locally; otherwise accuracy is unavailable. The archived reflection below includes historical outputs and descriptions that may differ from the final code. The current setup instructions above take precedence.

![Streamlit interface example](StreamLit%20Photos/Curious.png)

The project originated from a course scaffold in the `tcsai` organization. This personal copy preserves the supplied GPL-3.0 license and documents my course work and extensions; it does not claim that all scaffolding was authored by me.

---

## Original course narrative and final reflection

# Welcome
Welcome to my short but strong adventure in reproducibility! (Both you and my future self!)

## Some More About This Space

You might think of this small space as an introduction to ==shareable and clean== practices in code/project production.

This portfolio has been and is being evolved throughout a Research Seminar class held at the Tilburg University in 2025. So, since this is a learning adventure of a student, there might be some drawbacks. But still, I believe that you can learn a lot jeven just by navigating through the files and folders there.

Also as a bonus point: There's a weekly cycle of things held, which you may find under the "reports" folder, in case you might be interested in seeing a bit more.

Nevertheless, I will also provide a weekly summary of progression with bullet points below.

Final reflection (or the last report) of this journey can be found at the bottom of this file.

Enjoy!

### About Me
Hi again. *Still me*. I’m Ozan Safak Kocak, a student at the **Data Science and Society** Master's program at the Tilburg University.

#### Summary Guidance

**Week 1**
- Dive into real-world project setup, learn how to use github
- Go to github and create a repository
- Create issue on github and then close it
- Add buddy feature into your repository

**Week 2**
- Use Linux commands for direct transactions with the computer
- Create a mini project involving a data preparation script
- Git commands in terminal
- Makefile basics
- Install & Configure Ruff

**Week 3**
- In "processor.py" file (under "src" folder) you will find some trial codes. Don't be afraid! We've got you covered with our numpy style explanations.
- See the testing code of this code in "test_processor" file (under "tests") folder. "pytest.ini" (among the files in the scaffold) will tie these two files for you, don't worry about that.
- Just type "pytest -q" (without the quoting marks, of course) in your terminal and test my code, please.
- Keep an eye on here for the upcoming weeks and tips!

**Week 4**
- Find relevant context in .sandbox and environment.yml files
- Check Docker files for a first impression on creating docker images
- See requirements.txt file for parallel updates
- The peer feedback report is omitted from this personal copy. 

**Week 5**
- Go and explore the "data" folder in the scaffold
- Relevant code can be found under "src" folder
- Please make a parallel reading with "Makefile" and "requirements.txt"

**Week 6**
- Relevant code can be found in classify.py, api.py and app.py files
- Check Dockerfile
- See requirements.txt file for parallel updates
- Deploy and enjoy model serving


##### FINAL REPORT

**1.Repo In Sum**

This pipeline creates a template very basic app/ml model (that makes predictions). The relevant phases can be summarized as following:

- Make use of Github to keep track of the process
- Includes code to preprocess and then process data
- Includes tests to sanity check the written code and debug when necessary
- Create and deploy necessary environments
- Create a docker image for increased transferability and shareability
- Collect raw data (ingestion), extract info from web (scraping), transform (scale) your data and classify
- Create an API that would host your classified model so that your model handles requests and deploy your model on web via an app 

Below are presented some important pieces built throughout the course on a weekly basis. Some of them include necessary/advised instructions to run and expected outputs:

*Week 1*:

- Github setup: https://github.com/oskocak-cell/RMD.git (NOTE: This link takes you to another github. Since this was the task and the current repository had already been prepared, to prove this skill I had to give a link to an external github repo built by myself. Anything else built throughout this project is under this current repository.)

*Week 2*:

- A mini project for automating data preprocessing: https://github.com/oskocak-cell/book-genre-classifier/tree/main/my_project_week2 (Please note that this project is contained within another folder itself so that similar content produced afterward wouldn't contradict with the content of this project.)

*Week 3*:

- Files to try and experience how testing works (in python): https://github.com/oskocak-cell/book-genre-classifier/blob/main/src/processor.py 

https://github.com/oskocak-cell/book-genre-classifier/blob/main/tests/test_processor.py

To <u>run</u> testing (in terminal): pytest -q
<u>Expected output</u> output: 6 passed in 0.02s

*Week 4*:

- Creating environments: https://github.com/oskocak-cell/book-genre-classifier/blob/main/requirements.txt

<u>Run</u> this in your terminal outside any sandbox to get a global check whether numpy is installed: python -c "import numpy; print(numpy.__version__)"

<u>Expected output</u>: Sandboxes don’t leak into the global Python environment. If numpy isn't installed globally, this should fail.

- A configuration file for python packages: https://github.com/oskocak-cell/book-genre-classifier/blob/main/pyproject.toml 
- Dockerfile: https://github.com/oskocak-cell/book-genre-classifier/blob/main/Dockerfile

You need to <u>run</u> the docker image in your terminal with the following command: docker run reproducible-proj
<u>Expected output</u>: Running experiment...
<u>Numpy version: 2.3.3</u>
Computation: 6

(Please note that the output is just the expected one. So your numpy version might be different for instance.)

- IMPORTANT NOTE: The content of the work done in Week 4 had to be extended later (especially in Week 6) and altered when necessary. Thus, the Dockerfile was updated afterward and would serve the puposes of Week 6, rather than those of Week 4.

*Week 5*:

- Script to fetch and save raw HTML: https://github.com/oskocak-cell/book-genre-classifier/blob/main/src/fetch_data.py
- Script for parsing saved HTML: https://github.com/oskocak-cell/book-genre-classifier/blob/main/src/scrape_books.py
- Script for storing and scaling mentioned data: https://github.com/oskocak-cell/book-genre-classifier/blob/main/src/clean_books.py
- Script for classification: https://github.com/oskocak-cell/book-genre-classifier/blob/main/src/classify.py

*Week 6*:

- FastAPI Service: https://github.com/oskocak-cell/book-genre-classifier/blob/main/src/api.py

To <u>run</u> the API: uvicorn src.api:app --reload --port 8000
After you run the API, <u>run in another terminal tab/window</u>: curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{"text": "the grand design"}'
<u>Expected output</u>: {"prediction":"science"}

- Dockerfile changed to dockerize the API: https://github.com/oskocak-cell/book-genre-classifier/blob/main/Dockerfile
- A Streamlit App: https://github.com/oskocak-cell/book-genre-classifier/blob/main/src/app.py

<u>To run</u> the StreamLit APP: streamlit run src/app.py
<u>Expected output</u>: https://github.com/oskocak-cell/book-genre-classifier/blob/main/README.md#:~:text=StreamLit-,Photos

**2.Considerations on the Progress**

To elaborate more on the content presented above, it would be appropriate to comment on the various aspects of the process and tools used.

I believe that the punchline of this project is "compatibility and sustainability". In other words, as suggested by the course name: "reproducibility".

Let's take a closer look.

Throughout the process github was the main platform used. Github lets facilitates the workflow. Once you start a repository on github, every contributor can work by themselves and then add it to the pool where the main components of the project are developped. Using Linux commands is also crucial. Removing the "mediators" and interacting directly with the operating system provides the developer with more control on the workflow.

After these steps, there we dive into testing, debugging and object orientation. Object orientation is one of the most prominent concepts of programming. It allows you to create well-designed scripts. Nevertheless, since there are many contributors in a project, it is important that every contributor conducts a sanity check on the relevant component s/he creates, and that is done via testing and debugging.

Moreover, to run the code and necessary components of the project we need to create relevant environments locally. But then all the parts should be transferable between different tech tools. In other words, what I create runs well in my own computer and operating system. How do we make it work on other contributors' too taking different technologies and setups into account? That's exactly what Docker does.

After all these, we need to extract and classify the data -classify them so that our model can make predictions- and make it accessible by others through the model where mentioned data work inherently. For that purpose, we first need a hosting service (API) and then we need to deploy it on web through an app (StreamLit App in our project).

Above is a more detailed summary of the project and the process. Now, it is visible that we focus on a very substantial problem: "How do we work together and make our work understandable to each other and also to future interested parties?" Thus, in addition to all the tools mentioned above, we also need to employ methods to improve reproducibility. For instance, using dockstrings in coding is crucial for that reason. It improves the explainability and understandability of the code included.

Nevertheless, along the way, there are challenges, too. For example, Week 4 where we created environments was one of the most challenging parts of the project. I received many errors trying to create environments, because the relevant python package versions I deployed were more recent and it didn't run as expected.

This is just an example, but I think this can shed light on challenges faced and possible methods to overcome:
- It is crucial to understand what the problem is
- Read the error messages carefully
- Google it. You're not the only one or the first one having this problem most of the time.
- AI is also usable but be prudent. If it is AI only and you are not really understanding the problem and the solution, then you are not solving it in its real sense.

I believe that the project is highly reproducible. Still, some improvements could be possible. For instance, you might improve the variety of the predictions made by the model.

Lastly, if you were to run this project fom zero again, make sure that you arrange the Dockerfile accordingly. Docker was first deployed during Week 4, but then it was necessary to adapt it in Week 6. So, in case you run things built in Week 4 without adapting necessary changes in Dockerfile, it is possible that you might run into errors.

**3.Further Explorations**

Below is a list of further explorations conducted throughout the process:

- Buddy “feature branch” (as suggested in the first class.) "Since it was not possible to add a buddy to the current class repository, I had to test this feature on another repository on github." https://github.com/oskocak-cell/RMD/compare/feature/add-cli3?expand=1 

-As advised, I created a pyproject.toml and added [tool.ruff] section into it. https://github.com/oskocak-cell/book-genre-classifier/blob/main/my_project_week2/pyproject.toml

Also on a theoretical level, I tried to discover even more why the Linux is popular/important.

- I added some more codes to the DataProcessor class (in "processor.py") to create the median value for the dataset. Further, I added docstring explanations in numpy style along with my code, and I included the necessary testing codes in "test_processor.py". Also, while updating my README file, I tried to use some markdown cheatsheet.

https://github.com/oskocak-cell/book-genre-classifier/blob/main/src/processor.py
https://github.com/oskocak-cell/book-genre-classifier/blob/main/tests/test_processor.py
https://github.com/oskocak-cell/book-genre-classifier/blob/main/README.md

- I tried creating virtual environments with other versions of python than referred in the workbook.
https://github.com/oskocak-cell/book-genre-classifier/blob/main/requirements.txt 

- I included additional genres, in other words, I downloaded additional .html files belonging to other genres. https://github.com/oskocak-cell/book-genre-classifier/tree/main/StreamLit%20Photos#:~:text=StreamLit,-Photos 

- I added CLI arguments with argparse and extended the download to other book genres/categories. https://github.com/oskocak-cell/book-genre-classifier/blob/main/src/fetch_data.py 

- I added /metrics as an additional endpoint. https://github.com/oskocak-cell/book-genre-classifier/blob/main/src/api.py 

If I had more time, I would dive deeper into Linux. I think that using terminal opens the "computer's universe" and many possibilities. Moreover, I would try to improve prediction capabilities of the model. Trying and failing teach a lot. This effort would also serve my code testing skills.

**4.Peer-Feedback Inclusion**

Following peer feedback:

- I properly included self-explorations in weekly reports https://github.com/oskocak-cell/book-genre-classifier/tree/main/reports

- I didn't add images to show some outcomes as suggested in peer feedback. The main reason is that I believe that showing all or many outcomes via images would unnecessarily pollute my project scaffold.I wanted to keep my folder structure clean and precise as much as possible.

**5.GenAI Usage**

Thanks to this process, I increased my awareness in transparent AI using.

I mainly used AI to either understand some concepts further or solve problems faced. Rarely I asked for its support in creating things too. For instance, I asked for ChatGPT's help to set up [tool.ruff] in a pyproject.toml -> https://github.com/oskocak-cell/book-genre-classifier/blob/main/my_project_week2/pyproject.toml 

I believe that AI is not very useful in learning new concepts, because there is a huge variety of sources on the internet outside the AI world. Nevertheless, it might simplify complex concepts and thus make them more understandable.

AI is also useful in handling problems. But for any usage of AI it its really crucial to understand what the problem and the solution are. Otherwise, you either don't learn or you cannot even solve the problem, because it gives generic responses and then you should for instance adapt the AI's response to the problem you are dealing with.

**6.Final Considerations**

Even though mentioned as a "project" above, for experienced developers this must seem very tiny. Indeed it has many things but only as a prototype.

Still, I do believe that in essence, it serves the punchline, which is the stress on reproducibility!

During one of the classes, it was argued that one of the very reasons why reproducibility wasn't "popular" in worklife was that it was either "ego" or similar behavioral reasons. Honestly, that was a good learning point for me. This reminded me that no matter how good the tools could be, how humans deploy it could be even more crucial.

So, in essence, this tiny project could seem weak in terms of its complexity, but it is powerful in terms of the tools and how these tools are used. I would suggest the following few steps to turn it into a bigger project:

- Gather more people together
- Make sure that they have "similar" perspectives about reproducibility
- Let them suggest ideas and implement them through using these (or other) tools in a sustainable, communicable and explainable manner
- Make sure that these are sustainable, communicable and explainable not only for them, but also for others and future colleagues.

For instance, a team of developers could solidfy the prediction abilities of the model.