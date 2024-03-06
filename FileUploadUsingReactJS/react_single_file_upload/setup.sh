npm install
pushd $PWD
cd server
yarn add express multer cors nodemon axios
npm -g install nodemon

if [ ! -d "public" ]
then
	mkdir "public"
fi

nodemon ./server &
popd

npm start 

