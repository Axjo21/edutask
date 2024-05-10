describe('Attempting to setup prerequisite', () => {

    let uid // user id
    let name // name of the user (firstName + ' ' + lastName)
    let email // email of the user

    before(function () {
        cy.fixture('user.json')
            .then((user) => {
            cy.request({
                method: 'POST',
                url: 'http://localhost:5005/users/create',
                form: true,
                body: user
            }).then((response) => {
                uid = response.body._id.$oid
                name = user.firstName + ' ' + user.lastName
                email = user.email
            })
        })
    })

    beforeEach(function () {
    // enter the main main page
        cy.visit('http://localhost:3000')
    })

    it('starting out on the landing screen', () => {
    // make sure the landing page contains a header with "login"
        cy.get('h1')
            .should('contain.text', 'Login')
    })

    it('login to the system with an existing account', () => {
        cy.contains('div', 'Email Address')
            .find('input[type=text]')
            .type(email)

        cy.get('form')
            .submit()

        cy.get('h1')
            .should('contain.text', 'Your tasks, ' + name)
        })

        after(function () {
        // clean up by deleting the user from the database
        cy.request({
            method: 'DELETE',
            url: `http://localhost:5005/users/${uid}`
        }).then((response) => {
            cy.log(response.body)
        })
    })
})
