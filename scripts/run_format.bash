for path in $(find -name '*.md'); do
    python3 scripts/format.py $path
done;
