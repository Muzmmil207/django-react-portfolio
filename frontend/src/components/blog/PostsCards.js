import React from "react";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";

function PostsCards(props) {
  return (
    <Card className="project-card-view">
      <Card.Img variant="top" src={props.imgPath} alt="card-img" />
      <Card.Body>
        <Button variant="primary" href={props.poLink} target="_blank">
          {props.title}
        </Button>
      </Card.Body>
    </Card>
  );
}
export default PostsCards;
