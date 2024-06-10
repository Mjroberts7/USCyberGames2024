#!/bin/bash

file_path="$1"
output_file="computedHashesFile.txt"

# Check if file path is provided
if [ -z "$file_path" ]; then
  echo "Error: Please provide the path to the file as first argument"
  exit 1
fi

# md5 and sha algo's
algorithms=(md5 1 224 256 384 512 512224 512256)

# clears the output file in case we need to run this multiple times
> "$output_file"

# Checks each algo
for algorithm in "${algorithms[@]}"; do
  # Check if the specific hashing tool exists for the algorithm
  if [ "$algorithm" == "md5" ]; then 
    hash_value=$(md5sum "$file_path" | cut -d' ' -f1)
  else # Use shasum for commonly available algorithms
    hash_value=$(shasum -a "$algorithm" "$file_path" | cut -d' ' -f1)
  fi
  # writing the algo and hash value to the output file
  echo "$algorithm: $hash_value" >> "$output_file"
done

echo "Hash values saved to: $output_file"
