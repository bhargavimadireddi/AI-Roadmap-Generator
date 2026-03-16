def print_roadmap(career, roadmap):
    """
    Displays the roadmap in a clear, numbered step-by-step format.
    """
    print(f"\nOutput:")
    # print(f"\n--- Learning Roadmap for {career} ---")
    for i, step in enumerate(roadmap, 1):
        print(f"{i}. {step}")
    print()

def main():
    # Dictionary storing roadmaps for different careers.
    # Keys are stored in lowercase for easier case-insensitive matching.
    roadmaps = {
        "ai engineer": [
            "Learn Python",
            "Learn Mathematics for AI",
            "Learn Machine Learning",
            "Learn Deep Learning",
            "Build AI Projects"
        ],
        "data scientist": [
            "Learn Python or R",
            "Learn Statistics and Probability",
            "Master Data Manipulation (Pandas, SQL)",
            "Learn Data Visualization (Tableau, Matplotlib)",
            "Learn Machine Learning Algorithms",
            "Practice with Real-world Datasets"
        ],
        "web developer": [
            "Learn HTML & CSS",
            "Learn JavaScript",
            "Learn a Frontend Framework (React, Vue, or Angular)",
            "Learn Backend Development (Node.js, Python/Django, etc.)",
            "Learn Database Management (SQL, MongoDB)",
            "Build Full-Stack Web Projects"
        ]
    }

    print("Welcome to the AI Roadmap Generator!")
    print("Available careers: AI Engineer, Data Scientist, Web Developer\n")
    
    while True:
        # Prompt user for their career goal
        user_input = input("Input: ").strip().lower()
        
        if user_input == 'exit':
            print("Exiting... Good luck on your learning journey!")
            break
            
        # Check if the requested career exists in our dictionary
        if user_input in roadmaps:
            print_roadmap(user_input.title(), roadmaps[user_input])
        else:
            print(f"\nSorry, we don't have a roadmap for '{user_input.title()}' yet.")
            print("Please try one of the available careers (or type 'exit' to quit).\n")

if __name__ == "__main__":
    main()
