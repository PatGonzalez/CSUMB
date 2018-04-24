/**
 * 
 */

/**
 * @author cholmes
 *
 */
public class BarcodeImage implements Cloneable
{
   public static final int MAX_HEIGHT = 30;
   public static final int MAX_WIDTH = 65;
   private boolean[][] image_data;
   
   //Default constructor no params
   public BarcodeImage()
   {
      image_data = new boolean[MAX_HEIGHT][MAX_WIDTH];
      for ( int i=0; i < image_data.length; i++ )
      {
         for ( int j=0; j < image_data[i].length; j++ )
         {
            image_data[i][j] = false;
         }
      }
   }
   
   public BarcodeImage(String[] str_data)
   {
      //check to see if the string is of valid size, returns if its invalid
      if( !checkSize(str_data) )
      {
         return;
      }
      
      //Create an empty image_data, then loop through the string storing the corresponding true/false
      image_data = new boolean[MAX_HEIGHT][MAX_WIDTH];
      int dataLength = str_data.length - 1;
      for ( int i=MAX_HEIGHT-1; i >= 0; i-- )
      {
         for ( int j=0; j < MAX_WIDTH; j++ )
         {
            if( dataLength >= 0 )
            {
               char[] dataCharArray = str_data[dataLength].toCharArray();
               if( j < dataCharArray.length )
               {
                  if( dataCharArray[j] == DataMatrix.BLACK_CHAR )
                  {
                     image_data[i][j] = true;
                  }
                  else if ( dataCharArray[j] == DataMatrix.WHITE_CHAR )
                  {
                     image_data[i][j] = false;
                  }
               
               }
               else
               {
                  image_data[i][j] = false;
               }
            }
            else
            {
               image_data[i][j] = false;
            }
         }
         dataLength--;
      }            
   }
   
   //Accessor for pixel
   public boolean getPixel(int row, int col)
   {
      return image_data[row][col];      
   }
   
   //Mutator for pixel
   boolean setPixel(int row, int col, boolean value)
   {
      //checks to see if its a valid row and column, and sets the pixel if it is
      if(row < MAX_HEIGHT && 0 <= row && col < MAX_WIDTH && 0 <= col)
      {
         image_data[row][col] = value;
         return true;
      }
      else
      {
         return false;
      }
   }
   
   //Checks the incoming data for every conceivable size or null error
   private boolean checkSize(String[] data)
   {
      if(data == null || data.length > MAX_HEIGHT || data[0].length() > MAX_WIDTH)
      {
         return false;
      }
      return true;
   }
   

   //Displays the data to the console
   public void displayToConsole()
   {
      //Loops through each element in the 2d array, appending the corresping char to bool value
      for( int i = 0; i < MAX_HEIGHT; i++ )
      {
         StringBuilder data = new StringBuilder();
         for( int j = 0; j < MAX_WIDTH; j++ )
         {
            if(image_data[i][j] == true)
            {
               data.append(DataMatrix.BLACK_CHAR);
            }
            else if(image_data[i][j] == false)
            {
               data.append(DataMatrix.WHITE_CHAR);
            }
         }
         System.out.println(data);
      }
   }

   //Method that overrides the method of that name in Cloneable interface
   @Override
   public BarcodeImage clone() throws CloneNotSupportedException
   {
      BarcodeImage cloneImg = new BarcodeImage();
      cloneImg.image_data = image_data.clone();
      return cloneImg;
   }
}