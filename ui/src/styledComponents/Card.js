import styled from "styled-components";
import { rem } from "../hooks/rem";

export const Card = styled.div`
	background-color: #fff;
	box-shadow: 0px 20px 20px rgb(170 170 170 / 5%);
	border-radius: ${rem(30)}rem;
	padding: ${rem(15)}rem;
	margin: 0 2rem;
`;
export const IconGroup = styled.div`
	display: flex;
	justify-content: space-between;
`;
export const IconItem = styled.div`
	display: inline-flex;
	align-items: center;
	column-gap: 0.5rem;
`;
