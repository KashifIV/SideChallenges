#include <iostream> 
#include <dirent.h> 
#include <cstring> 
#include <fstream> 
#include <cstdlib> 
#include <vector> 
#include <map>  

using namespace std; 
bool checkType (string file) 
{
	if (file == "database.txt") 
		return false; 
	
	else if(file[file.size()-1] == 't' && file[file.size()-2] == 'x' && file[file.size()-3] == 't' && file[file.size()-4] == '.') 
		return true; 
	else 
		return false; 
}

vector<string> words(string line) 
{
	vector<string> val(0); 
	string w; 
	int a; 
	if (line[0] == ' ') 
		a = 1; 
	else 
		a = 0; 
	for (int i = a; i < line.size(); i++) 
	{
		
		if (line[i] == ' ') {
			if (w != "") 
				val.push_back(w); 
			w = ""; 
		} 
		else if((line[i] >= 65 && line[i] < 91)||(line[i] >= 97 && line[i] < 123))
		{
			w+= line[i]; 
		}
	}
	if (w != "")
		val.push_back(w);

	//for (int i = 0; i < val.size(); i++) 
		//cout << val[i] << " ";  
	//cout << endl; 
	return val; 
}
struct List
{
	vector<string> fileName; 
	vector< vector<int> > iterations; 
	vector< vector<int> > lineNumber; 
};
int main(int argc, char** argv)
{
 
	if (argc == 2 && std::string(argv[1]) == "--make-index")
	{
		cout << "WORKING" << endl; 
		ofstream out("database.txt"); 
		struct dirent *dir; 
		DIR *d; 
		d = opendir("."); 
		map<string, List> search;
		map<string, List> :: iterator iter; 
		List a;
		vector <int> b; 
		if (d)
		{
			int fileCounter = 0; 
			while((dir = readdir(d)) != NULL)
			{
				string name = dir->d_name; 
				if (checkType(name))
				{
					iter = search.begin(); 
					int currentLine = 0; 
					ifstream in; 
					in.open(name.c_str());	
					
					while(!in.eof())
					{
						string val; 
						getline(in, val); 
						vector<string> vals = words(val); 
						currentLine++; 
						for (int i= 0; i < vals.size(); i++) 
						{
							iter = search.find(vals[i]); 
							if (iter == search.end()) 
							{
								search.insert(make_pair(vals[i], a)); 
								iter = search.find(vals[i]); 
								iter->second.fileName.push_back(name); 
								iter->second.iterations.push_back(b); 
								iter->second.lineNumber.push_back(b); 
								
								int num =1; 
								for (int o = i+1; o < vals.size(); o++) 
								{
									if (vals[i] == vals[o]) 
									{
										num++; 
										vals.erase(vals.begin() + o); 
									}
								}
								iter->second.iterations[iter->second.iterations.size()-1].push_back(num);  
								iter->second.lineNumber[iter->second.iterations.size()-1].push_back(currentLine);
							}
							else 
							{
								
								int num =1; 
								for (int o = i+1; o < vals.size(); o++) 
								{
									if (vals[i] == vals[o]) 
									{
										num++; 
										vals.erase(vals.begin() + o); 
									}
								}
								if(iter->second.fileName[iter->second.fileName.size()-1] != name) 
								{
									iter->second.fileName.push_back(name); 
									iter->second.iterations.push_back(b); 
									iter->second.lineNumber.push_back(b); 
								}
								iter->second.iterations[iter->second.iterations.size()-1].push_back(num);  
								iter->second.lineNumber[iter->second.iterations.size()-1].push_back(currentLine);
							}
						}
					}
				}
				fileCounter++; 
			}
			cout << "FINISHED FETCHING..." << endl;
	
			iter = search.begin(); 
			//cout <<iter->second.fileName.size() << " " << iter->second.iterations.size(); 
			out << search.size() << endl; 
			while(iter != search.end())
			{
				//cout << iter->first << endl; 
				out << iter->first << " " << iter->second.fileName.size() << " "; 
				//cout << '\t'; 
				for (int i = 0; i < iter->second.fileName.size(); i++) 
				{
					//cout << iter->second.fileName[i] << " ";
					out << iter->second.fileName[i] << " ";
					out <<iter->second.iterations[i].size() << " ";
					for (int j = 0; j < iter->second.iterations[i].size(); j++) {
						//cout << iter->second.iterations[i][j] << " " << iter->second.lineNumber[i][j] << " ";
						out << iter->second.iterations[i][j] << " " << iter->second.lineNumber[i][j] << " "; 
					}
				}
				//cout << endl; 
				out << endl; 
				*iter++; 
			}
			cout << "DONE IMPORTING" << endl; 
		}
		else
			cout << "ERROR: CANNOT ACCESS DIRECTOR" << endl; 
	}
	else 
	{
		ifstream in("database.txt"); 
		int n; 
		in >> n; 
		for (int o = 1; o < argc; o++) 
		{
			bool found = false; 
			for (int l = 0; l < n; l++) 
			{
				string line; 
				in >> line; 
				if(argv[o] == line)
				{
					found = true; 
					int a; 
					in >> a; 
					cout << argv[o] << endl; 
					for (int i= 0; i < a; i++) 
					{
						string fileName; 
						in >> fileName; 
						cout << "Found in File: " << fileName << endl; 
						
						int b; 
						in >> b; 
						for (int j = 0; j < b; j++) 
						{
							int c, d; 
							in >> c >> d; 
							if (j == 0)
								cout << '\t' << "at line: " << d; 
							else 
								cout << ", and line: " << d; 
							if (c > 1) 
								cout << " (" << c << " times)"; 
							
						}
						cout << endl; 						
					}
					break; 
				}
				
				getline(in, line); 
			}
			if (!found) 
				cout << "\t Not Found." << endl; 
		}
	}
}