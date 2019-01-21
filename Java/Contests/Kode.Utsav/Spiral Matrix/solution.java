import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class Solution{
 static int  m_st =-1, n_st =-1, dir = 1;
 static int i = 0, j=0, s=0;
 static int m_end, n_end ;
 static boolean proceed = true;
 public static void update() {
        if (dir == 1) {
            if (j <  n_end-1) {
                j++;
            }
            else {
                if  (i == m_end-1) {
                    proceed = false;
                }
                else {
                dir = 2;
                i++;
                m_st++;
                }
            }
            }
        else if (dir == 2){
            if (i <  m_end-1) {
                i++;
            }
            else {
                if (j == n_st +1)
                {proceed = false;
                }
            else {
                dir = 3;
                j--;
                n_end--;
            }
            }
        }
        else if (dir == 3){
            if (j >  n_st+1) {
                j--;
            }
            else {
                if (i == m_st+1) {
                    proceed = false;
                }
                else {
                dir = 4;
                i--;
                m_end--;
                }
            }
        }
        else {
            if (i >  m_st+1) {
                i--;
            }
            else {
                if (j == n_end-1) {
                    proceed = false;
                }
                else {
                dir = 1;
                j++;
                n_st++;
                }
            }
        }
        }

 public static void main(String [] args) {
    Scanner sc = new Scanner(System.in);
     m_end = sc.nextInt();
     n_end = sc.nextInt();
    int [] spiral_arr = new int[m_end*n_end];
    int[][] arr = new int[m_end][n_end];
    for(int i=0; i< m_end; i++) {
    for(int j=0; j< n_end; j++) {
        arr[i][j] = sc.nextInt();
    }
    }
    while (proceed) {
        spiral_arr[s] = arr[i][j];
        update();
        s++;
    }
    for(int k=0; k< s;k++) {
        System.out.printf("%d ",spiral_arr[k]);
    }
 }
}
