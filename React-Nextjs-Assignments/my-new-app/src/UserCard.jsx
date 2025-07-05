import React from "react";
import UserDetails from "./UserDetails";

function UserCard({user}){
    return (
        <div style={styles.card}>
            <h2>{user.name}</h2>
            <UserDetails age={user.age} email={user.email} city={user.city} college={user.college} />
        </div>
    )
}

const styles = {
  card: {
    backgroundColor: 'white',
    borderRadius: '10px',
    padding: '20px',
  }
};

export default UserCard;