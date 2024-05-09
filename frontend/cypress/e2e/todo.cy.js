describe('Toggling the icon', () => {

    beforeEach(function () {
        cy.visit('http://localhost:3000')
    })



    it('Toggling the icon', () => {
        cy.contains('div', 'Email Address')
            .find('input[type=text]')
            .type(email)


    cy.get('form')
        .submit()

    cy.get('h1')
        .should('contain.text', 'Your tasks, ' + name)
    })

    after(function () {
    cy.request({
        method: 'DELETE',
        url: `http://localhost:5000/users/${uid}`
    }).then((response) => {
        cy.log(response.body)
    })
    })
})
