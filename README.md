# Data-Visualization-LLM-Agent

## 👁️ Overview

This project develops an **LLM-driven conversational agent** for business data. It translates natural language into optimized SQL, executes queries, and visualizes the results. Our goal is to make data exploration accessible to non-technical users and reduce the data querying effort for analysts by up to 60-70%.

-----

## 🚀 Key Features

  * **Natural Language to SQL:** An LLM-powered translator generates optimized SQL statements from plain English queries.
  * **Dynamic Visualizations:** Query results are returned as dynamic charts (bar, pie, line graphs) or tables.
  * **Multi-Turn Conversations:** The agent supports follow-up questions and context retention using short-term and long-term memory.
  * **Ambiguity Handling:** Prompts users for clarification on vague or incomplete queries.
  * **Safe Execution:** A backend SQL engine with robust logic to sanitize inputs and handle errors gracefully.
  * **Optional Python Code Generation:** The system can generate code snippets for advanced analysis, time permitting.

-----

## 👨‍💻 Getting Started for Developers

### 1\. Cloning the Repository

To get a local copy of this project, open your terminal and run the following command. 

```bash
git clone https://github.com/sky4320/Data-Visualization-LLM-Agent/
```

Then, navigate into the project directory:

```bash
cd Data-Visualization-LLM-Agent
```

### 2\. Switching to the Development Branch (`dev`)

All active development happens on the `develop` branch. After cloning, you need to switch to it from the default `main` branch.

```bash
git checkout develop
```

### 3\. Standard Workflow

Always pull the latest changes before you start working to avoid conflicts.

```bash
git pull origin develop
```

For every new feature, bug fix, or task, create a new branch from `develop`. This keeps our development branch clean and helps with code reviews.

```bash
git checkout -b feature/your-feature-name develop
```

Once you’ve made your changes, stage and commit them.

```bash
git add .
git commit -m "feat: [Your descriptive commit message]"
```

Finally, push your branch to the remote repository. The first time, use the `-u` flag.

```bash
git push -u origin feature/your-feature-name
```

After your work is complete, create a Pull Request on GitHub to merge your feature branch into the **`develop`** branch.

-----

## 🗺️ Project Milestones

| Milestone | Due Date |
| :--- | :--- |
| Finalize project scope, select dataset, and assign team roles | July 3, 2025 |
| Set up a development environment and tools | July 7, 2025 |
| Integrate LLM to translate natural language queries into SQL | July 11, 2025 |
| Build SQL execution layer connected to the chosen database | July 14, 2025 |
| Develop the visualization module for output display | July 18, 2025 |
| Design and build the UI | July 23, 2025 |
| Implement error handling, fallback messages, query validation | July 26, 2025 |
| Conduct system integration and end-to-end testing | July 31, 2025 |
| Prepare final demo and presentation materials | August 5, 2025 |
| Final Polishing and Rehearsal | August 8, 2025 |

-----

## 👥 Team

| Name | Role | Email |
| :--- | :--- | :--- |
| **Haris Ahmed** | Project Lead | hxa230007@utdallas.edu |
| **Niharika Balabommala** | LLM & Natural Language Processor | niharikapd12@gmail.com |
| **Jihye Choi** | Frontend & UI, Integration & Testing | dal516092@utdallas.edu |
| **Venkata Swetha Meghana Duvvuri** | LLM & Natural Language Processor, Integration & Testing | vduvvuri4954@muleriders.sauag.edu |
| **Veerabrahmam Veeravalli** | Visualization & Data Interpretation, Frontend & UI | veerabrahmamveeravalli@my.unt.edu |
| **Siva Keshav Yalamandala** | Database & Query Execution | sivakeshavyalamandala@gmail.com |

**Team Name:** QueryVision
**Mentor:** Manish Jain

-----

## 🛠️ Required Resources

  * **Development Platforms:** Google Colab, Visual Studio Code
  * **Version Control:** GitHub
  * **Frontend:** Streamlit
  * **LLM Integration:** HuggingFace Transformers, OpenAI API, or Text2SQL-T5
  * **Database:** SQLite or PostgreSQL (Chinook or IMDB dataset)
  * **Visualization Libraries:** Plotly, Matplotlib, or Seaborn
  * **Datasets:** Kaggle open datasets
  * **Collaboration Tools:** Google Docs
  * **APIs:** OpenAI or HuggingFace inference APIs for LLM functionality
