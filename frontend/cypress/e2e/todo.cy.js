describe('Toggling the icon', () => {

    beforeEach(function () {
        cy.visit('http://localhost:3000')
    })

    cy.get('div:first').should('have.class', 'container-element').click()

    it('Toggling the icon', () => {
        cy.get('.popup-inner')

    })
})
