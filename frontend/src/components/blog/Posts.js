import { Container, Row, Col } from "react-bootstrap";
import PostsCard from "./PostsCards";
import Particle from "../Particle";
import React, { useState, useEffect, useContext } from "react";

function Posts() {
  const [blogPosts, setBlogPosts] = useState([]);
  let getPostsData = async () => {
    let response = await fetch(`http://127.0.0.1:8000/api/users-messages/`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      }
    })
    let data = await response.json()
    setBlogPosts(data)
  }

  return (
    <Container fluid className="project-section">
      <Particle />
      <Container>
        <h1 className="project-heading">
          My Recent <strong className="purple">Posts </strong>
        </h1>
        <p style={{ color: "white" }}>
          Here are a few posts I've published recently.
        </p>
        <Row style={{ justifyContent: "center", paddingBottom: "10px" }}>

          {blogPosts.map((post) => {
            <Col md={4} className="project-card">
              <PostsCard
                imgPath={post.imageUrl}
                title={post.name}
                poLink={post.url}
              />
            </Col>
          })}

        </Row>
      </Container>
    </Container>
  );
}

export default Posts;
