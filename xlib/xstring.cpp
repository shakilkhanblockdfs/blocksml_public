/*
Copyright (C) 2009-2017 Free Software Foundation, Inc.

Written by Shakil A Khan <shakilk1729@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street - Fifth Floor, Boston, MA 02110-1301, USA.
*/

#include <xstring.h>
#include <iostream>
#include <sstream>
#include <list>
#include <vector>
#include <xunistd.h>

using namespace std;


void xstrcpy(xstring &dest, const xstring &src)
{
	dest = src.substr(0, src.length());
}

void xstrcpy(xstring &dest, const xstring &src, size_t len)
{
	dest = src.substr(0, MIN(src.length(),len));
}


vector<xstring> xsplit(const xstring &hay_string, const xstring &needle)
{
        xstring item;
        int delim_size = needle.size();
        int found = 0;
        int start_index = 0;
        vector<xstring>split_string;

	if (hay_string.size() == 0)
		return split_string;

        while( found != (int)xstring::npos)
        {
                found = (hay_string.substr(start_index)).find(needle);
                if( found != (int)xstring::npos )
                {
                        item = hay_string.substr(start_index, found);
                        start_index += found + delim_size;
                        if(item.size() >0)
                                split_string.push_back(item);
                }
                else
                {
                        item = hay_string.substr(start_index, found);

                        split_string.push_back(item);
                }
        }

  return split_string;
}

vector<xstring> xsplit(const xstring &hay_string)
{
	return xsplit(hay_string, xstring(" "));
}

string xstrstr(const xstring &haystack, const xstring &needle)
{
    size_t pos = haystack.find(needle);
    if (pos != std::xstring::npos)
        return haystack.substr(pos);
    return xstring("");
}

string xstrnstr(const xstring &haystack, const xstring &needle, size_t len)
{
	xstring lhaystack(haystack);
	lhaystack = lhaystack.substr(0, len);

    size_t pos = lhaystack.find(needle);
    if (pos != std::xstring::npos)
        return haystack.substr(pos);
    return xstring("");
}

//Modifies the original string
void xtoupper(xstring &s)
{
    std::transform(s.begin(),s.end(), s.begin(), ::toupper);
}

//Modifies the Original string
void xtolower(xstring &s)
{
    std::transform(s.begin(),s.end(), s.begin(), ::tolower);
}

//Returns a newly constructed substring
string xstrcasestr(const xstring &haystack, const xstring &needle)
{
    xstring lhaystack(haystack);
    xstring lneedle(needle);

    xtolower(lhaystack);
    xtolower(lneedle);

    size_t pos = lhaystack.find(lneedle);
    if (pos != std::xstring::npos)
        return haystack.substr(pos);
    return xstring("");
}

