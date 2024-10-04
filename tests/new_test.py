# from core.models.assignments import AssignmentStateEnum, GradeEnum


# def test_get_assignments(client, h_clerk):
#     """
#     failure case: clerk is not in the database hence, he cannot access the assignments
#     """
#     response = client.get(
#         '/clerk/assignments',
#         headers=h_clerk
#     )

#     assert response.status_code == 404

def test_root_url(client):
    response = client.get('/')

    assert response.status_code == 200

def test_post_assignment_student_2(client, h_student_2):
    content = 'ABCD TESTPOST 2'

    response = client.post(
        '/student/assignments',
        headers=h_student_2,
        json={
            'content': content
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['content'] == content
    assert data['state'] == 'DRAFT'
    assert data['teacher_id'] is None

def test_post_edit_assignment_student_1(client, h_student_1):
#    """
#     failure case: id does not exist in database hence
#     """
    content = 'ABCD TESTPOST 3'

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'id': 8,
            'content': content
        })

    assert response.status_code == 404