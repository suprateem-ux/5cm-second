name: Lichess Team Manager

on:
  workflow_dispatch:        # allows manual trigger from GitHub UI
  schedule:
    - cron: "0 15 * * *"    # optional: runs daily at 3 PM UTC (8:30 PM IST)

jobs:
  manage-teams:
    runs-on: ubuntu-latest

    env:
      LICHESS_TOKEN: ${{ secrets.LICHESS_TOKEN }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests

      - name: Display message file
        run: |
          echo "===== Message content from d.txt ====="
          cat d.txt || echo "(d.txt not found)"
          echo "======================================"

      - name: Run Lichess Team Manager
        run: python team_manager.py

      - name: Done
        run: echo "✅ Workflow completed successfully."
