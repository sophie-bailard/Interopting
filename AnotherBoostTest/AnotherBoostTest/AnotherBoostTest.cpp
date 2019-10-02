#include <string>
#include <iostream>
#include <boost/foreach.hpp>

int main()
{
	std::string str("Hello Boost!\n");
	BOOST_FOREACH(char ch, str)
	{
		std::cout << ch;
	}
	return 0;
}