import penman

def validate_amr_file(file_path):
    
    with open('Mapped_CatalanAnnotations.txt', 'r', encoding='utf-8') as file:
        # Split annotations by double newline
        annotations = file.read().strip().split("\n\n")

    print(f"Found {len(annotations)} AMR annotations to validate.\n")

    for idx, annotation in enumerate(annotations, start=1):
        print(f"Validating AMR #{idx}...")
        try:
            # Attempt to decode the AMR annotation
            graph = penman.decode(annotation)
            print(f"AMR #{idx} is valid!\n")
        except Exception as e:
            print(f"AMR #{idx} is invalid!")
            print(f"Error: {e}\n")
            
# Call the function with your file
validate_amr_file("Mapped_GreekAnnotations.txt")
