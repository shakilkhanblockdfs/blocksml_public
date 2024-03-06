
export ABBYY_APPID=ee08fd6c-0be5-4d02-95e1-3e7da7d82771
export ABBYY_PWD=u8ewJVb0fzyNYeh+lWnD1Zzu

if [ $# -ne 1 ]
then
	echo "Please enter the file name to process"
	exit 1
fi

python process.py $1 $1__result.txt
