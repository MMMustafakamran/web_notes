import fitz
import os
import io
import time
import sys
from PIL import Image

# Force UTF-8 for stdout to avoid encoding errors with progress bars
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Initialize EasyOCR Reader
def get_ocr_reader():
    """Initializes EasyOCR. Note: may download models on first run."""
    try:
        import easyocr
        # Use English. gpu=False for better compatibility.
        reader = easyocr.Reader(['en'], gpu=False)
        return reader
    except Exception as e:
        print(f"EasyOCR initialization info: {e}")
        return None

def process_pdf(pdf_path, reader):
    print(f"Processing: {os.path.basename(pdf_path)}")
    start_time = time.time()
    
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF {pdf_path}: {e}")
        return

    base_path = os.path.splitext(pdf_path)[0]
    output_md = base_path + "_content.md"
    image_dir = base_path + "_images"
    
    if not os.path.exists(image_dir):
        os.makedirs(image_dir, exist_ok=True)
        
    md_content = [f"# Content from {os.path.basename(pdf_path)}\n"]
    
    for i, page in enumerate(doc):
        md_content.append(f"## Page {i+1}\n")
        
        # 1. Native Text Extraction
        text = page.get_text().strip()
        is_ocr = False
        
        # 2. OCR Fallback if text is sparse or missing
        if (not text or len(text) < 50) and reader:
            try:
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                img_data = pix.tobytes("png")
                results = reader.readtext(img_data, detail=0)
                ocr_text = " ".join(results).strip()
                if ocr_text:
                    text = (text + "\n\n" if text else "") + ocr_text
                    is_ocr = True
            except Exception as e:
                print(f"  OCR skipped for page {i+1} due to error: {e}")
        
        if is_ocr:
            md_content.append(text + "\n\n*(Extracted via OCR)*\n")
        else:
            md_content.append(text + "\n")
        
        # 3. Image Extraction
        try:
            image_list = page.get_images(full=True)
            if image_list:
                md_content.append("\n### Images:\n")
                for img_index, img in enumerate(image_list):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    ext = base_image["ext"]
                    img_name = f"page_{i+1}_img_{img_index + 1}.{ext}"
                    img_path = os.path.join(image_dir, img_name)
                    
                    with open(img_path, "wb") as f:
                        f.write(image_bytes)
                    
                    md_content.append(f"![{img_name}]({os.path.basename(image_dir)}/{img_name})\n")
        except Exception as e:
            print(f"  Error accessing images on page {i+1}: {e}")
        
        md_content.append("\n---\n")
    
    with open(output_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md_content))
    
    doc.close()
    elapsed = time.time() - start_time
    print(f"Done! Created: {os.path.basename(output_md)} ({elapsed:.1f}s)")

def main():
    # Recursively find and process all PDFs in 'lecture slides'
    search_dir = r"c:\Users\dynamic computer\Desktop\work\FAST\semester 7\webdev\notes\lecture slides"
    reader = get_ocr_reader()
    
    pdf_files = []
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))
    
    print(f"Found {len(pdf_files)} PDF files.")
    for pdf_path in pdf_files:
        try:
            process_pdf(pdf_path, reader)
        except Exception as e:
            print(f"Critical error on {pdf_path}: {e}")

if __name__ == "__main__":
    main()
