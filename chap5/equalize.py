import cv2

try:
  # OpenCVの輝度平滑化関数はグレイスケール画像が対象のため、グレイスケール化
  img = cv2.imread('img/Lenna.jpg', cv2.IMREAD_GRAYSCALE)
  if img is None:
    print('ファイルを読み込めません')
    import sys
    sys.exit()
  
  dst = cv2.equalizeHist(img)
  cv2.imwrite('img/equalizeHist.jpg', dst)
  cv2.imshow('img', dst)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
except:
  import sys
  print("Error:", sys.exc_info()[0])
  print(sys.exc_info()[1])
  import traceback
  print(traceback.format_tb(sys.exc_info()[2]))