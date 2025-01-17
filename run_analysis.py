import subprocess

# List of scripts to run in sequence
scripts = ["dataset_prep.py", "feature_eng.py", "knowledge_graph.py"]

for script in scripts:
    try:
        print(f"Running {script}...")
        # Execute the script
        subprocess.run(['python', script], check=True)
        print(f"Completed {script} successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script}. Exiting pipeline.\n")
        break

print("Pipeline execution completed.")