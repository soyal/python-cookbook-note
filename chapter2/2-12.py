# 审查清理文本字符串
#
import sys
import unicodedata
s = 'pýtĥöñ\fis\tawesome\r\n'
# ord将字符转为unicode point
# chr将unicode point 转为字符
remap = {
  ord('\t'): ' ',
  ord('\f'): ' ',
  ord('\r'): None
}

sr = s.translate(remap)
print(sr)


cmb = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
srb = unicodedata.normalize('NFD', sr)
print('after: ', srb.translate(cmb)) # after:  python is awesome