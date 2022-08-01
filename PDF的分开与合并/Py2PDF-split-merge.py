from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter

def merge(input1,input2,output):

    file_merger = PdfFileMerger()
    file_merger.append(input1)
    file_merger.append(input2)
    file_merger.write(output)

def split(input,output,start_page, end_page):
    try:
        read_file = input
        fp_read_file = open(read_file, 'rb')
        pdf_input = PdfFileReader(fp_read_file)  # 将要分割的PDF内容格式话
        page_count = pdf_input.getNumPages()  # 获取PDF页数
        print("该文件共有{}页".format(page_count))  # 打印页数

        try:
            print(f'开始分割{start_page}页-{end_page}页，保存为{output}......')
            pdf_output = PdfFileWriter()  # 实例一个 PDF文件编写器
            for i in range(start_page, end_page):
                pdf_output.addPage(pdf_input.getPage(i))
            with open(output, 'wb') as sub_fp:
                pdf_output.write(sub_fp)
            print(f'完成分割{start_page}页-{end_page}页，保存为{output}!')
        except IndexError:
            print(f'分割页数超过了PDF的页数')
        # fp.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # input1 = open(r"1.pdf", "rb") #打开第一个PDF文件
    # input2 = open(r"2.pdf", "rb") #打开第二个PDF文件
    # output=r'submit.pdf'
    # merge(input1,input2,output)

    input = r"C:\Users\admin\Desktop\mapreduce.pdf"  #打开第二个PDF文件
    output= r'1.pdf'
    split(input,output,2,9) # start 起始页 从0 开始算，end 是尾页从1开始算