import cv2

try:
  # どのような画像であってもグレイスケールで読み込む
  img = cv2.imread('img/Lenna.jpg', cv2.IMREAD_GRAYSCALE)
  if img is None:
    print('ファイルを読み込めません')
    import sys
    sys.exit()
  
  cv2.imwrite('img/grayscale.jpg', img)

  cv2.imshow('img', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
except:
  import sys
  print("Error:", sys.exc_info()[0])
  print(sys.exc_info()[1])
  import traceback
  print(traceback.format_tb(sys.exc_info()[2]))