export PYTHONPATH=$PYTHONPATH:$(pwd)/scripts
python ai_lab_repo.py \
    --research-topic="Long-horizon mobile manipulation in robotics" \
    --note-path="note.json" \
    --copilot-setting-file="copilot_settings.json" \
    --llm-backend="gemini-2.0-flash" \
    --compile-pdf \
    --max-steps=100 \
    --num-papers-lit-review=15 \
    --papersolver-max-steps=5 \
    --mlesolver-max-steps=3 

    # --load-existing \
    # --load-existing-path="" \
