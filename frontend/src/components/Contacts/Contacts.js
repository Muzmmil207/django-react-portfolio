import { Container, Row, Col } from "react-bootstrap";
import React from "react";
// import Particle from "../Particle";

function Contacts() {
    let sendUsersMessage = async (e) => {
        e.preventDefault()
        let response = await fetch('http://127.0.0.1:8000/contacts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 'email': e.target.email.value, 'message': e.target.message.value })
        })
        let data = await response.json()
        e.target.email.value = ''
        e.target.message.value = ''
        console.log(data)
    }
    const handleSubmit = (e) => {
        sendUsersMessage(e)
    }


    return (
        <Container fluid className="project-section">
            {/* <Particle /> */}
            <Container>
                <h1 className="project-heading">
                    My Recent <strong className="purple">Works </strong>
                </h1>
                <Row style={{ justifyContent: "center", paddingBottom: "10px" }}>

                    <Col md={4} className="project-card">
                        <form onSubmit={handleSubmit}>
                            <div className="form-group">
                                <input type="text" className="form-control" name="email" placeholder="Enter email" />
                            </div>
                            <div className="form-group">
                                <textarea type="text" className="form-control" name="message" placeholder="Enter Message" />
                            </div>
                            <input type="submit" className="btn btn-primary" />
                        </form>
                    </Col>

                </Row>
            </Container>
        </Container>
    );
}

export default Contacts;
