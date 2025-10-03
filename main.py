# AI Q&A Bot - Command Line Interface
# This bot uses Hugging Face Transformers to answer questions

import os
from transformers import pipeline
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def initialize_qa_bot():
    """
    Initialize the question-answering pipeline using Hugging Face
    
    This function creates a pipeline that can answer questions based on context.
    We're using a pre-trained model that doesn't require an API key.
    """
    print("🤖 Initializing AI Q&A Bot...")
    print("📚 Loading Hugging Face model (this may take a moment)...")
    
    try:
        # Create a question-answering pipeline
        # This uses a free pre-trained model from Hugging Face
        qa_pipeline = pipeline(
            "question-answering",
            model="distilbert-base-cased-distilled-squad",
            tokenizer="distilbert-base-cased-distilled-squad"
        )
        
        print("✅ Bot initialized successfully!")
        return qa_pipeline
        
    except Exception as e:
        print(f"❌ Error initializing bot: {e}")
        return None

def get_context():
    """
    Get context from user or use a default context
    
    Context is the information the bot will use to answer questions.
    """
    print("\n📖 Please provide some context (text) that the bot can use to answer questions.")
    print("Or press Enter to use the default context about Python programming.")
    
    user_context = input("\nEnter your context: ").strip()
    
    if not user_context:
        # Default context about Python programming
        user_context = """
        Python is a high-level, interpreted programming language with dynamic semantics. 
        It was created by Guido van Rossum and first released in 1991. Python's design 
        philosophy emphasizes code readability with its notable use of significant whitespace. 
        Its language constructs and object-oriented approach aim to help programmers write 
        clear, logical code for small and large-scale projects. Python is dynamically-typed 
        and garbage-collected. It supports multiple programming paradigms, including structured, 
        object-oriented and functional programming. Python is often described as a "batteries 
        included" language due to its comprehensive standard library. It is used for web 
        development, data science, artificial intelligence, automation, and many other applications.
        """
        print("📝 Using default context about Python programming.")
    
    return user_context

def ask_questions(qa_pipeline, context):
    """
    Main interaction loop where user asks questions
    
    Args:
        qa_pipeline: The initialized Hugging Face pipeline
        context: The context text to answer questions from
    """
    print("\n🎯 You can now ask questions about the provided context!")
    print("💡 Type 'quit', 'exit', or 'bye' to stop the bot.")
    print("📄 Type 'context' to see the current context again.")
    print("-" * 50)
    
    while True:
        # Get user question
        question = input("\n❓ Your question: ").strip()
        
        # Check for exit commands
        if question.lower() in ['quit', 'exit', 'bye', 'q']:
            print("\n👋 Thanks for using the AI Q&A Bot! Goodbye!")
            break
        
        # Show context if requested
        if question.lower() == 'context':
            print(f"\n📖 Current context:\n{context}")
            continue
        
        # Skip empty questions
        if not question:
            print("⚠️ Please enter a question.")
            continue
        
        try:
            print("🤔 Thinking...")
            
            # Get answer from the AI model
            result = qa_pipeline(question=question, context=context)
            
            # Display the answer
            answer = result['answer']
            confidence = result['score']
            
            print(f"\n🤖 Answer: {answer}")
            print(f"📊 Confidence: {confidence:.2%}")
            
            # Provide feedback on confidence level
            if confidence > 0.8:
                print("✅ High confidence answer!")
            elif confidence > 0.5:
                print("⚡ Moderate confidence answer.")
            else:
                print("⚠️ Low confidence - the answer might not be accurate.")
                
        except Exception as e:
            print(f"❌ Error getting answer: {e}")

def main():
    """
    Main function that runs the AI Q&A Bot
    """
    print("=" * 50)
    print("🚀 AI Q&A Bot - Powered by Hugging Face")
    print("=" * 50)
    
    # Step 1: Initialize the AI model
    qa_pipeline = initialize_qa_bot()
    
    if qa_pipeline is None:
        print("❌ Failed to initialize bot. Exiting...")
        return
    
    # Step 2: Get context from user
    context = get_context()
    
    # Step 3: Start the question-answering loop
    ask_questions(qa_pipeline, context)

if __name__ == "__main__":
    main()