# -*- coding: utf-8 -*-

### 09. [Typoglycemia](https://en.wikipedia.org/wiki/Typoglycemia)
# Cho đầu vào là một câu tiếng Anh bao gồm các word ngăn cách nhau bằng ký tự space. Viết chương trình thực hiện việc sau:
# - Với mỗi word, giữ nguyên ký tự đầu và ký tự cuối, đảo thứ tự một cách ngẫu nhiên các ký tự còn lại của (tất nhiên các word có ít hơn 4 ký tự thì không cần làm gì)
# - Cho trước một câu tiếng Anh hợp lệ, ví dụ "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .", chạy chương trình đã viết để đưa ra kết quả.

def typoglycemia(s):
    # TODO: implement the function
    news = s
    return news

def main():
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    print "Original string: %s" % s
    print "Typoglycemia string: %s" % typoglycemia(s)


if __name__ == '__main__':
    main()    
    

    

    
    
    
