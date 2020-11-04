import io from 'socket.io-client';

const connection = () => {
    return io.connect("localhost:3000");
}

export default connection;
