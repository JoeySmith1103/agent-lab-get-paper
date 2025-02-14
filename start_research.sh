export PYTHONPATH=$PYTHONPATH:$(pwd)/scripts
python ai_lab_repo.py \
    --research-topic="Long-horizon mobile manipulation in robotics" \
    --note-path="note.json" \
    --copilot-setting-file="copilot_settings.json" \
    --llm-backend="gemini-2.0-flash" \
    --compile-pdf \
    --max-steps=100 \
    --num-papers-lit-review=5 \
    --papersolver-max-steps=5 \
    --mlesolver-max-steps=3 \
    # --load-existing \
    # --load-path="state_saves/literature_review.pkl"

# NOTE: Please use the following command to execute the script
# script -c "bash start_research.sh" -f research_log.txt