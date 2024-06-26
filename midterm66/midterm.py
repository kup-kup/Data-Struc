from math import sqrt

#2
'''
ให้ class LinkedList มาแบบแหว่ง จงเติมให้เต็ม
(insert append prepend ...)
ที่สำคัญคือ reverse
'''

#3
'''
ก --- ทำ sequential search
ข --- ทำ sort และ binary search

ถ้า list(ความยาว n) ไม่ได้เรียงมา จงวิเคราะห์ว่าแบบไหนเร็วกว่า พร้อมอธิบายเหตุผล
1) สำหรับการทำครั้งเดียว
2) สำหรับการทำ n ครั้ง(เท่ากับจำนวนของใน list)
'''

#4
#queue จาก 2 stack
'''
ให้เขียน class queue ขึ้นมาโดยไม่ให้ใช้ tail attribute แต่มี stack มาให้ใช้ 2 อันแทน
'''

#5
#เศรษฐากับถุงเท้า
'''
นายเศรษฐาต้องการแยกคู่ถุงเท้าของเขาหลังจากซักเสร็จ โดยถุงเท้ามีอยู่ n คู่ ถุงเท้าแต่ละคู่จะมีลายไม่ซ้ำกัน 
สามารถใช้โครงสร้างข้อมูลใดนการช่วยจับคู่ถุงเท้าให้ทำงานได้อย่างมีประสิทธิภาพ
ให้เขียนโปรแกรมแสดงการทำงานแยกถุงเท้าพร้อมวิเคราะห์ความเร็วในการทำงาน
'''

#6
#แถวซื้อของ
'''
(โจทย์อาจะไม่เปะแต่ประมาณนี้)
ในห้างแห่งหนึ่งมีเคาน์เตอร์สำหรับชำระเงิน n เคาน์เตอร์ และลูกค้าที่ต้องการชำระเงินอยู่ m คน
โดยแต่ละเคาน์เตอร์ใช้เวลาในการชำระเงินต่างกัน(ให้ assume ว่าจำนวนของที่แต่ละคนซื้อมีจำนวนเท่ากัน)
โจทย์ต้องการให้เขียนโปรแกรม(python หรือ pseudocode) สำหรับคำนวณหาเวลาที่สั้นที่สุดในการชำระเงินลูกค้าทั้งหมด
พร้อมกับวิเคราะห์ความเร็วในการทำงาน

(ตัวอย่าง)
มีอยู่ 4 เคาน์เตอร์และลูกค้า 9 คน

เคาน์เตอร์     เวลาในการชำระเงิน    จำนวนลูกค้าเพื่อ
            ต่อหนึ่งคน(นาที)      เวลาที่เร็วที่สุด
1           7                  1
2           2                  4
3           3                  2
4           4                  2

เวลาที่เร็วที่สุดจะเป็น 8 นาที
'''