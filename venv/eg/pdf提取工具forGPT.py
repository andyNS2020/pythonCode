#pdf解析提取
import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        i = 0
        for page in pdf.pages:
            i+=1
            print(i)
            text += page.extract_text()
    return text

# 提取PDF文档中的文本内容
#pdf_text = extract_text_from_pdf("/Users/Andy/Desktop/XX银行核心业务系统POC测试方案V1.0.pdf")
pdf_text = extract_text_from_pdf("/Users/Andy/Downloads/dall-e-3技术文档.pdf")
print(pdf_text)