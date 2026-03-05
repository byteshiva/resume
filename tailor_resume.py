
import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: python tailor_resume.py <path_to_job_description> <output_filename>")
        sys.exit(1)

    job_description_path = sys.argv[1]
    output_filename = sys.argv[2]

    with open("archives/cv.adoc", "r") as f:
        resume = f.read()

    with open(job_description_path, "r") as f:
        job_description = f.read()

    # This is where you would integrate with an LLM
    # For example, you could use the OpenAI API

    prompt = f"""
    Here is a resume:
    {resume}

    Here is a job description:
    {job_description}

    Please rewrite the resume to be more tailored to the job description.
    Focus on the skills and experience that are most relevant to the role.
    The output should be in the same format as the original resume.
    """

    output_path = os.path.join("tailored_resumes", output_filename)
    with open(output_path, "w") as f:
        f.write(prompt)

    print(f"Tailored resume saved to {output_path}")

if __name__ == "__main__":
    main()
