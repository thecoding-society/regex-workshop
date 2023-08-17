import re
import sys

def main():
    input_url = input("Enter the Instagram profile URL: ")
    extracted_id = extract_insta_id(input_url)
    if extracted_id:
        print("Extracted Instagram ID:", extracted_id)
    else:
        print("Invalid URL format")


def extract_insta_id(url):
    # Code Here


if __name__ == "__main__":
    main()
