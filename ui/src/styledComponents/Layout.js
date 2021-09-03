import styled from "styled-components";

export const Container = styled.div`
	margin: ${({ margin }) => margin && margin};
`;
export const Header = styled.header`
	width: 100%;
	position: fixed;
	bottom: 0;
	left: 0;
	border-radius: ${30 / 16}rem;
	box-shadow: 0px 2px 20px 0px hsla(0, 0%, 0%, 0.05);
	height: ${115 / 16}rem;
	background-color: #fff;
	z-index: 1;
`;
