import { Typographic } from "../../styledComponents/Global";
import { Container } from "../../styledComponents/Layout";
import { CardContainer } from "../../reusableComponents/Card/index";
import { Carousel } from "../Carousel/Carousel.jsx";

export const Home = () => {
	return (
		<Container margin="1.5rem 1.5rem 8.5rem 1.5rem">
			<Typographic color="title" fontSize={24} fontWeight={700} lineHeight={31}>
				Enjoy our Delicius pizzas
			</Typographic>
			<Typographic color="title" fontSize={16} fontWeight={700} lineHeight={21}>
				Our pizza of the day
			</Typographic>
			<CardContainer pizzaOfTheDay={true} />
			<Typographic color="title" fontSize={16} fontWeight={700} lineHeight={21}>
				Our popular pizzas
			</Typographic>
			<Carousel />
		</Container>
	);
};
