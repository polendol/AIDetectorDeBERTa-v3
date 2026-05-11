from transformers import pipeline
import os

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
#the model
pipe = pipeline("text-classification", model="vraj33/ai-text-detector-deberta")

chunk_size = 1000 #100 characters, 150-200 words
model_name = pipe

def main():
    #the user personalizes the input file and the report name file
    file_in = input(str("Introduce the name of your file: "))
    file_out = input(str("Introduce the name of your report file: "))
    input_file = str(file_in + ".txt")
    output_file = str(file_out + ".txt")

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please create it first.")
        return

    # Chunks splitting
    chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]

    #Visualize that the program is running
    print(f"Analysing {len(chunks)} chunks using DeBERTa-v3...")

    #report creation
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("AI DETECTION REPORT\n")
        out.write(f"Model used: {model_name}\n")
        out.write(f"Total Chunks: {len(chunks)}\n\n")

        for i, chunk in enumerate(chunks):
            print(f"Analyzing chunk {i + 1}/{len(chunks)}...")
            result_coded = model_name(chunk)
            label_coded = result_coded[0]["label"] #real or AI, O = human, 1 =  AI
            if label_coded == "LABEL_0":
                label = "AI"
            elif label_coded == "LABEL_1":
                label = "Human"
            else:
                label = "Unrecognised"

            score = result_coded[0]["score"] #how confident the model is about the label

            out.write(f"--- CHUNK {i + 1} ---\n")
            out.write(f"TEXT: {chunk[:100].replace('\n', ' ')}...\n")
            out.write(f"LABEL:\n{label}\n\n")
            out.write(f"SCORE:\n{score}\n\n")
            out.write("*" * 50 + "\n\n")

    print(f"Analysis complete. Report saved to {output_file}")


if __name__ == '__main__':
    main()