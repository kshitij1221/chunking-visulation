from typing import List
import re
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

def paragraph_chunker(text: str) -> List[str]:
    # Split text into paragraphs based on double newlines
    paragraphs = re.split(r'\n{2,}', text.strip())
    return [paragraph.strip() for paragraph in paragraphs if paragraph.strip()]
def sentence_chunker(text: str, sentences_per_chunk: int) -> List[str]:
    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    chunks = []


    #create function with text to split into sentences and group into chunks of specified number of sentences
    
    
    # Group sentences into chunks
    for i in range(0, len(sentences), sentences_per_chunk):
        chunk_sentences = sentences[i: i + sentences_per_chunk]
        chunk = ' '.join(chunk_sentences)
        chunks.append(chunk)
    
    return chunks

# Example usage
if __name__ == "__main__":
    text = (
        "Machine learning is a subset of artificial intelligence. It focuses on .building systems that learn from data and improve over time.\n\n"
        "Applications include healthcare, finance, and robotics. Advanced techniques like neural networks are key to its success."
    )
    
    #Generate paragraph-based chunks
    # chunks = sentence_chunker(text, 2)
    # print("Sentence-based chunks:")
    # print(chunks)
    # print(len(chunks))
    # print("\n")
    chunks = sentence_chunker(text, 1)

    #Display chunks
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i}:\n{chunk}\n")