# Agent Laboratory

## Introduction

Agent Laboratory is an end-to-end autonomous research workflow meant to assist you as the human researcher toward implementing your research ideas using LLMs. 
* **No API Costs**: This project exclusively uses Gemini 2.0 Flash's free API, so you don't need to worry about OpenAI or other paid LLMs.  

## Installation

1. Create a codna environment

    ```bash
    conda create --name "agent-lab" python=3.12
    conda activate agent-lab
    ```

2. Install requirements

    ```bash
    pip install -r requirements.txt
    ```

3. Install `pdflatex` [OPTIONAL, but recommended]

    ```bash
    sudo apt-get install texlive-latex-base
    sudo apt-get install texlive-fonts-recommended
    sudo apt-get install texlive-fonts-extra
    sudo apt-get install texlive-latex-extra
    pdflatex --version  # Check if installed
    ```

## Run

Before running the code, you should do some configurations.

0. Add your `GEMINI_API_KEY` to `.env` file
1. Setup `copilot_settings.json` to configure which phases the human should be involved in.
    * true: human is involved
    * false: human is not involved

2. Setup `note.json` to add your notes to let LLM know more about the task and provide better quality results.

    (NOTICE: Please follow the format of the example in `note.json` or you can check the json schema in `scripts/json_validator.py`)

3. Setup `start_research.sh` to configure the parameters

4. Use the following command to run the code

    ```bash
    script -c "bash start_research.sh" -f research_log.txt
    ```

## Disclaimer

This project is not the official version of the original repository. It is a modified version of [AgentLaboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) and is not affiliated with or maintained by the original author. For more details, please refer to the original repository.
