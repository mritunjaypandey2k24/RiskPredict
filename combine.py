import os

output_file_path = os.path.join(os.getcwd(), 'best_rf_model.pkl')  # Path to save the reassembled file in the current directory
input_dir = r'C:\Users\MRITUNJAY\Downloads\Chunk'  # Directory where the chunks are stored

with open(output_file_path, 'wb') as output_file:
    chunk_num = 0
    while True:
        chunk_file_path = os.path.join(input_dir, f'chunk_{chunk_num}.pkl')
        if not os.path.exists(chunk_file_path):
            break
        with open(chunk_file_path, 'rb') as chunk_file:
            output_file.write(chunk_file.read())
        chunk_num += 1

print(f'Successfully reassembled the file from {chunk_num} chunks')
