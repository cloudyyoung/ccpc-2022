import java.time.Year;
import java.util.Hashtable;
import java.util.Scanner;

public class e {
    public static void main(String args[]){
 //     String input = "20 20 2\n10 2 +\n10 18 -";
        Scanner sc = new Scanner(System.in);
        String firstLine = sc.nextLine();
        String[] splitStr = firstLine.split("\\s+");
        int numX = Integer.parseInt(splitStr[0]);
        int numY = Integer.parseInt(splitStr[1]);
        int numOfPar = Integer.parseInt(splitStr[2]);
        // int numX = 20;
        // int numY = 20;
        // int numOfPar = 2;
        char[][] result = new char[numX][numY];
        Particle[] particles = new Particle[numOfPar];
        for(int i = 0; i<numOfPar;i++){
            String line = sc.nextLine();
            String[] split = line.split("\\s+");
            int x = Integer.parseInt(split[0]);
            int y = Integer.parseInt(split[1]);
            Particle newP = new e().new Particle(x, y, split[2]);
            particles[i] = newP;
            if(split[2].equals("+")){
                result[y-1][x-1] = '+';
            }else{
                result[y-1][x-1] = '-';
            }
        }
        // Particle one = new e().new Particle(10,2,'+');
        // Particle two = new e().new Particle(10,18,'-');
        // result[1][9] = '+';
        // result[17][9] = '-';
        // particles[0] = one;
        // particles[1] = two;
        for(int i = 0; i<numX;i++){
            for(int j =0; j<numY;j++){
                if(result[i][j] == '\0')
                    result[i][j] = calculate(particles, i+1,j+1);
                System.out.print(result[i][j]);
            }
            System.out.println();
        }
    }
    

    public static char calculate(Particle[] particles, int x, int y){
        double t1 = 1.0/Math.PI;
        double t2 = 1.0/((Math.PI)*(Math.PI));
        double t3 = 1.0/((Math.PI)*(Math.PI)*(Math.PI));
        double value = 0;
        for(int i = 0;i<particles.length;i++){
            int particleX = particles[i].x;
            int particleY = particles[i].y;
            int particleSign = particles[i].sign;
            value = value + (1/distance(particleX, particleY, x, y))*particleSign;
        }
        if(value<=(-1*t1)) return '%';
        else if(value>(-1*t1)&&value<=(-1*t2)) return 'X';
        else if(value>(-1*t2)&&value<=(-1*t3)) return 'x';
        else if(value>(-1*t3)&&value<t3) return '.';
        else if(value>=t3&&value<t2) return 'o';
        else if(value>=t2&&value<t1) return 'O';
        else return '0';
    }

    public static double distance(int ParticleX, int ParticleY, int x, int y){
        double rx = Math.abs(ParticleX-x);
        double ry = Math.abs(ParticleY-y);
        return Math.sqrt(rx*rx+ry*ry);
    }
    class Particle{
        public int x;
        public int y;
        public int sign;

        public Particle(int iy, int ix, String s){
            x = ix;
            y = iy;
            if(s.equals("+")){
                sign = 1;
            }else{
                sign = -1;
            }
        }
    }
}
