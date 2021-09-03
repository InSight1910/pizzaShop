import styled from "styled-components";

export const BottomBar = styled.nav`
	display: flex;
	justify-content: space-between;
	margin: 1rem;
`;
export const NavLink = styled.a`
	${({ background }) => background && `background: var(${background})`};
	${({ borderRadius }) => borderRadius && `border-radius: ${borderRadius}%`};
	padding: 1rem;
	display: inline-flex;
`;
