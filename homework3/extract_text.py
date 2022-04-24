from PIL import Image
import pytesseract as pt
import os
      
def main(path, tempPath):
    # path for the folder for getting the raw images
    #path ="/Users/zahinroja/Downloads/data/aljazeera_2000px/07"
  
    # path for the folder for getting the output
    #tempPath ="/Users/zahinroja/Downloads/data/aljazeera_text/07"
  
    # iterating the images inside the folder
    for imageName in os.listdir(path):
              
        inputPath = os.path.join(path, imageName)
        img = Image.open(inputPath)
  
        # applying ocr using pytesseract for python
        text = pt.image_to_string(img, lang ="eng")
  
        # for removing the .jpg from the imagePath
        #imagePath = imagePath[0:-4]
  
        fullTempPath = os.path.join(tempPath, 'time_'+imageName+".txt")
        #print(text)
  
        # saving the  text for every image in a separate .txt file
        file1 = open(fullTempPath, "w")
        file1.write(text)
        file1.close() 
  
if __name__ == '__main__':

    #aljazeera
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/08', '/Users/zahinroja/Downloads/data/aljazeera_text/08')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/09', '/Users/zahinroja/Downloads/data/aljazeera_text/09')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/10', '/Users/zahinroja/Downloads/data/aljazeera_text/10')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/11', '/Users/zahinroja/Downloads/data/aljazeera_text/11')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/12', '/Users/zahinroja/Downloads/data/aljazeera_text/12')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/13', '/Users/zahinroja/Downloads/data/aljazeera_text/13')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/14', '/Users/zahinroja/Downloads/data/aljazeera_text/14')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/15', '/Users/zahinroja/Downloads/data/aljazeera_text/15')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/16', '/Users/zahinroja/Downloads/data/aljazeera_text/16')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/17', '/Users/zahinroja/Downloads/data/aljazeera_text/17')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/18', '/Users/zahinroja/Downloads/data/aljazeera_text/18')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/19', '/Users/zahinroja/Downloads/data/aljazeera_text/19')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/20', '/Users/zahinroja/Downloads/data/aljazeera_text/20')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/21', '/Users/zahinroja/Downloads/data/aljazeera_text/21')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/22', '/Users/zahinroja/Downloads/data/aljazeera_text/22')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/23', '/Users/zahinroja/Downloads/data/aljazeera_text/23')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/24', '/Users/zahinroja/Downloads/data/aljazeera_text/24')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/25', '/Users/zahinroja/Downloads/data/aljazeera_text/25')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/26', '/Users/zahinroja/Downloads/data/aljazeera_text/26')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/27', '/Users/zahinroja/Downloads/data/aljazeera_text/27')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/28', '/Users/zahinroja/Downloads/data/aljazeera_text/28')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/29', '/Users/zahinroja/Downloads/data/aljazeera_text/29')
    main('/Users/zahinroja/Downloads/data/aljazeera_2000px/30', '/Users/zahinroja/Downloads/data/aljazeera_text/30')

    #fox
    main('/Users/zahinroja/Downloads/data/fox_2000px/12', '/Users/zahinroja/Downloads/data/fox_text/12')
    main('/Users/zahinroja/Downloads/data/fox_2000px/13', '/Users/zahinroja/Downloads/data/fox_text/13')
    main('/Users/zahinroja/Downloads/data/fox_2000px/14', '/Users/zahinroja/Downloads/data/fox_text/14')
    main('/Users/zahinroja/Downloads/data/fox_2000px/15', '/Users/zahinroja/Downloads/data/fox_text/15')
    main('/Users/zahinroja/Downloads/data/fox_2000px/16', '/Users/zahinroja/Downloads/data/fox_text/16')
    main('/Users/zahinroja/Downloads/data/fox_2000px/17', '/Users/zahinroja/Downloads/data/fox_text/17')
    main('/Users/zahinroja/Downloads/data/fox_2000px/18', '/Users/zahinroja/Downloads/data/fox_text/18')
    main('/Users/zahinroja/Downloads/data/fox_2000px/19', '/Users/zahinroja/Downloads/data/fox_text/19')
    main('/Users/zahinroja/Downloads/data/fox_2000px/20', '/Users/zahinroja/Downloads/data/fox_text/20')
    main('/Users/zahinroja/Downloads/data/fox_2000px/21', '/Users/zahinroja/Downloads/data/fox_text/21')
    main('/Users/zahinroja/Downloads/data/fox_2000px/22', '/Users/zahinroja/Downloads/data/fox_text/22')
    main('/Users/zahinroja/Downloads/data/fox_2000px/23', '/Users/zahinroja/Downloads/data/fox_text/23')
    main('/Users/zahinroja/Downloads/data/fox_2000px/24', '/Users/zahinroja/Downloads/data/fox_text/24')
    main('/Users/zahinroja/Downloads/data/fox_2000px/25', '/Users/zahinroja/Downloads/data/fox_text/25')
    main('/Users/zahinroja/Downloads/data/fox_2000px/26', '/Users/zahinroja/Downloads/data/fox_text/26')
    main('/Users/zahinroja/Downloads/data/fox_2000px/27', '/Users/zahinroja/Downloads/data/fox_text/27')
    main('/Users/zahinroja/Downloads/data/fox_2000px/28', '/Users/zahinroja/Downloads/data/fox_text/28')
    main('/Users/zahinroja/Downloads/data/fox_2000px/29', '/Users/zahinroja/Downloads/data/fox_text/29')
    main('/Users/zahinroja/Downloads/data/fox_2000px/30', '/Users/zahinroja/Downloads/data/fox_text/30')
    main('/Users/zahinroja/Downloads/data/fox_2000px/31', '/Users/zahinroja/Downloads/data/fox_text/31')

    #cnn
    main('/Users/zahinroja/Downloads/data/cnn_2000px/01', '/Users/zahinroja/Downloads/data/cnn_text/01')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/02', '/Users/zahinroja/Downloads/data/cnn_text/02')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/03', '/Users/zahinroja/Downloads/data/cnn_text/03')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/04', '/Users/zahinroja/Downloads/data/cnn_text/04')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/05', '/Users/zahinroja/Downloads/data/cnn_text/05')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/06', '/Users/zahinroja/Downloads/data/cnn_text/06')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/07', '/Users/zahinroja/Downloads/data/cnn_text/07')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/08', '/Users/zahinroja/Downloads/data/cnn_text/08')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/09', '/Users/zahinroja/Downloads/data/cnn_text/09')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/10', '/Users/zahinroja/Downloads/data/cnn_text/10')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/11', '/Users/zahinroja/Downloads/data/cnn_text/11')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/12', '/Users/zahinroja/Downloads/data/cnn_text/12')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/13', '/Users/zahinroja/Downloads/data/cnn_text/13')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/14', '/Users/zahinroja/Downloads/data/cnn_text/14')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/15', '/Users/zahinroja/Downloads/data/cnn_text/15')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/16', '/Users/zahinroja/Downloads/data/cnn_text/16')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/17', '/Users/zahinroja/Downloads/data/cnn_text/17')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/18', '/Users/zahinroja/Downloads/data/cnn_text/18')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/19', '/Users/zahinroja/Downloads/data/cnn_text/19')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/20', '/Users/zahinroja/Downloads/data/cnn_text/20')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/21', '/Users/zahinroja/Downloads/data/cnn_text/21')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/22', '/Users/zahinroja/Downloads/data/cnn_text/22')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/23', '/Users/zahinroja/Downloads/data/cnn_text/23')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/24', '/Users/zahinroja/Downloads/data/cnn_text/24')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/25', '/Users/zahinroja/Downloads/data/cnn_text/25')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/26', '/Users/zahinroja/Downloads/data/cnn_text/26')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/27', '/Users/zahinroja/Downloads/data/cnn_text/27')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/28', '/Users/zahinroja/Downloads/data/cnn_text/28')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/29', '/Users/zahinroja/Downloads/data/cnn_text/29')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/30', '/Users/zahinroja/Downloads/data/cnn_text/30')
    main('/Users/zahinroja/Downloads/data/cnn_2000px/31', '/Users/zahinroja/Downloads/data/cnn_text/31')

