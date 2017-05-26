#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//----------------- Metodos ----------------

double distanciaPuntos (double x0, double y0, double xi, double yi )
{
	double dist=(pow(x0-xi,2))+(pow(y0-yi,2));
	return pow(dist,0.5);
}

double radioMax (double x0, double y0, double *x, double *y,int n)
{
	double radio=distanciaPuntos(x0, y0, x[0], y[0]);
	double radio_next;
	for (int i=0; i<n;i++)
		{
			radio_next=distanciaPuntos(x0, y0, x[i], y[i]);
			if(radio_next<radio)
				{
					radio=radio_next;
				}
		}
	return radio-1;
}

int main()
{
	//---------------- Declaracion de variables -------------
	int i;
	int a;
	int n=42;	//El numero de datos en cada documento

	double likelihood;   //Calcula el parecido de los puntos anterior y actual
	double alpha; 		
	double x0;
	double y0;
	double r0;
	double xi;
	double yi;
	double ri;
	double walk=0.2;


	//---------------- PUNTEROS--------------//
	FILE *data;
	data=fopen("Canal_ionico.txt","r");
	FILE *data1;
	data1=fopen("Canal_ionico1.txt","r");
	double *x;              //Esta va a ser la lista de todos los x del archivo
	x=malloc(84*sizeof(double));
	double *y;              //Esta es la lista de todos los y del archivo
	y=malloc(84*sizeof(double));

//-----------------Eso es para el primer grupo de datos
	for(i=0;i<42;i++)
		{						//Para imprimir la lista con los valores de x y y
			fscanf(data1,"%lf %lf\n",&x[i],&y[i]);
			//printf("%lf %lf\n",x[i],y[i]);
		}

	// Inicializar todos los datos x,y del centro del circulo
	x0=0;
	y0=0;
	r0=radioMax(x0,y0,x,y,n);
	for(i=0;i<3000;i++)		//Intentar con 20000 iteraciones
	{
		xi=x0+(drand48()*2.0*walk)-walk;
		yi=y0+(drand48()*2.0*walk)-walk;
		ri=radioMax(xi,yi,x,y,n);
		likelihood=ri/r0;
		if(likelihood>1.0)
		{
			//Aumenta el tamaño del circulo por lo tanto es mas optimo
			x0=xi;
			y0=yi;
			r0=ri;
		}
		else
		{
			alpha=drand48();
			if(alpha<likelihood)
			{
				x0=xi;
				y0=yi;
				r0=ri;
			}
		}
		printf("%lf %lf %lf\n",x0,y0,r0);//Los primeros 3000 datos
	}
//----------------------------para el segundo grupo de datos
	for(i=0;i<42;i++)
		{						//Para imprimir la lista con los valores de x y y
			fscanf(data,"%lf %lf\n",&x[i],&y[i]);
			//printf("%lf %lf\n",x[i],y[i]);
		}

	// Inicializar todos los datos x,y del centro del circulo
	x0=0;
	y0=0;
	r0=radioMax(x0,y0,x,y,n);
	for(i=0;i<3000;i++)		//Intentar con 20000 iteraciones
	{
		xi=x0+(drand48()*2.0*walk)-walk;
		yi=y0+(drand48()*2.0*walk)-walk;
		ri=radioMax(xi,yi,x,y,n);
		likelihood=ri/r0;
		if(likelihood>1.0)
		{
			//Aumenta el tamaño del circulo por lo tanto es mas optimo
			x0=xi;
			y0=yi;
			r0=ri;
		}
		else
		{
			alpha=drand48();
			if(alpha<likelihood)
			{
				x0=xi;
				y0=yi;
				r0=ri;
			}
		}
		printf("%lf %lf %lf\n",x0,y0,r0);//Los ultimos 2000 datos
	}
}