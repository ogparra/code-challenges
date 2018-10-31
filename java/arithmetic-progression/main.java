import java.util.Arrays;
import java.io.*;


class Main {
  public static void main(String[] args) {
    
    try{ 
      // to read the contents of the file
          BufferedReader br = new BufferedReader(new FileReader("test.txt"));
          int testCases = Integer.parseInt(br.readLine());

          while(testCases > 0){
            br.readLine(); // length of test array
            int[] test = convertToIntArray(br.readLine());
            int result = determineArithmeticProgression(test);
            System.out.println("Missing value is: "+ result);
            testCases--;
          } 
          
    }catch(IOException e){
      System.out.println("An exception was thrown, we could no find the file you were searching for.");
    }
  }

  // Input: Integer test array
  // Returns: Missing element in A.P.
  // if no missing number returns -1 
  public static int determineArithmeticProgression(int[] test){
    
    if(test.length < 3){
      System.out.println("Array is too short");
      return -1;
    }else{
      int l = 0;
      int r = test.length - 1;
      int m = (l+r)/2;

      int dist1 = test[m] - test[m-1];
      int dist2 = test[m+1] - test[m];

      int p = Math.min(dist1, dist2); // arithmetic progression value

      for(int i = 0; i < test.length-1; i++){
        int exValue = test[i] + p;
        if(exValue == test[i+1]){
          continue;
        }else{
          return exValue;
        }
      }
      // no missing integer from list provided
      return -1;
    }
  }

  // Takes as input a string and converts to a string array
  // Converts the string array to an int array
  public static int[] convertToIntArray(String str){
    // Convert string to string array using a space delimiter
    String[] stringArray = str.split(" ");
    int[] intArray = new int[stringArray.length];

    // refactor with higher order map function
    for(int i = 0; i < stringArray.length; i++){ 
      intArray[i] = Integer.parseInt(stringArray[i]);
    }
    
    return intArray;
  }
}