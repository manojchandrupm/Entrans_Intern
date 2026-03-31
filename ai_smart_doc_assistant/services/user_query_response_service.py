import ollama
import asyncio

async def generate_query_response(content):
    # context = ""
    # for msg in content['matches']:
    #     context+=msg['text']
    context = "\n\n".join([match["text"] for match in content['matches']])
    prompt = f"""
            You are an AI assistant for question answering.

You are given:
1. A user question
2. Top retrieved context chunks from a document (each chunk may include page or chunk id)

Your task:
- Answer the question ONLY using the provided context.
- Do NOT use any external knowledge.
- If the answer is not present in the context, say:
  "I don't know based on the provided document."

Instructions:
- Be clear and concise.
- Do not hallucinate or assume anything.
- If the answer is found in multiple chunks, combine the information.

MANDATORY:
- You MUST include source references.
- Mention the chunk number and/or page number from which the answer is taken.
- If multiple chunks are used, list all relevant sources.

Output format:
Answer: <your answer>
Sources: <Chunk X, Page Y>

---

User Question:
{content['question']}

---

Context:
{context}

---

Answer:
            """

    try:
        answer = await asyncio.to_thread(
            lambda: ollama.chat(
                model="llama3:8b",
                messages=[{"role": "user", "content": prompt}]
            )['message']['content']
        )
    except Exception as e:
        answer = "Error generating answer: " + str(e)

    return answer
