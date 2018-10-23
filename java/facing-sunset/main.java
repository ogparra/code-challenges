import java.util.Arrays;
import java.io.*;


class Main {
  public static void main(String[] args) {
    
    int facingSunset = 0;
    try{ 
      // to read the contents of the file
          BufferedReader br = new BufferedReader(new FileReader("test1.txt"));
          int testCases = Integer.parseInt(br.readLine());

          while(testCases >= 0){
            // Determine number of buildings
            // Convert the string to a int array
            //int numBuildings = Integer.parseInt(br.readLine());
            br.readLine();
            int[] buildings = convertToIntArray(br.readLine());
            testCases--;
          } 
          
    }catch(IOException e){
      System.out.println("An exception was thrown, we could no find the file you were searching for.");
    }
  }

  // Converts a string array to 
  public static int[] convertToIntArray(String buildings){
    // Convert string to string array using a space delimiter
    String[] buildingStrArr = buildings.split(" ");
    System.out.println(Arrays.toString(buildingStrArr));
    System.out.println(buildingStrArr[0]);
    int[] buildingsIntArr = new int[buildingStrArr.length];

    // for(int i = 0; i < buildingStrArr.length; i++){ 
    //   buildingsIntArr[i] = Integer.parseInt(buildingStrArr[i]);
    // }
    
    return buildingsIntArr;
  }
}



