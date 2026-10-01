# simlist

A dataset of simulation frameworks for large agent systems, with a web view.

Run:

    python3 serve.py

This opens http://localhost:8000/. The page reads `frameworks_general.csv`, `frameworks_coding.csv`, `frameworks_specialised.csv`, `runs.csv` and `resources.csv` every 2 seconds. Edit a CSV and save it. The page shows the change. You do not need to rebuild or reload.

In the framework CSVs, the `costs` cell is a JSON list of `[value, unit, description]` triples. Each description is a verbatim quote from the official paper or repository.

Each framework value comes from the framework's arXiv paper or its official GitHub repository. `evidence.csv` gives the verbatim quote and the source URL for each value.

General purpose frameworks do not fix the type of system: the user defines the environment or the task. Coding harnesses (system type "software engineering") are in `frameworks_coding.csv`. All other frameworks are in `frameworks_specialised.csv`.

`runs.csv` lists runs of each framework reported in other papers, one row per run, with the number of agents, costs, or both. Each size, cost and `uses_quote` is a verbatim quote from the paper at `source`. In the framework CSVs, `largest_size_any_paper` gives the largest of these runs.
